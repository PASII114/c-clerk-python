import pygame
import sys
import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

# ==========================
# Chess engine (rules + AI)
# ==========================

FILES = 'abcdefgh'
RANKS = '12345678'

WHITE, BLACK = 0, 1
EMPTY = '.'

PIECES = {
    'P','N','B','R','Q','K',
    'p','n','b','r','q','k'
}

# Piece values for evaluation
VAL = {
    'P': 100, 'N': 320, 'B': 330, 'R': 500, 'Q': 900, 'K': 0,
    'p': -100, 'n': -320, 'b': -330, 'r': -500, 'q': -900, 'k': 0,
}

# Piece-square tables (middle game, simplified)
PST_W = {
    'P': [
        0,  0,  0,  0,  0,  0,  0,  0,
        50,50,50,50,50,50,50,50,
        10,10,20,30,30,20,10,10,
        5, 5,10,25,25,10, 5, 5,
        0, 0, 0,20,20, 0, 0, 0,
        5,-5,-10, 0, 0,-10,-5, 5,
        5,10,10,-20,-20,10,10, 5,
        0, 0, 0, 0, 0, 0, 0, 0],
    'N': [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50],
    'B': [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20],
    'R': [
          0,  0,  0,  0,  0,  0,  0,  0,
          5, 10, 10, 10, 10, 10, 10,  5,
        - 5,  0,  0,  0,  0,  0,  0, -5,
        - 5,  0,  0,  0,  0,  0,  0, -5,
        - 5,  0,  0,  0,  0,  0,  0, -5,
        - 5,  0,  0,  0,  0,  0,  0, -5,
        - 5,  0,  0,  0,  0,  0,  0, -5,
          0,  0,  0,  5,  5,  0,  0,  0],
    'Q': [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
         -5,  0,  5,  5,  5,  5,  0, -5,
          0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20],
    'K': [
         20, 30, 10,  0,  0, 10, 30, 20,
         20, 20,  0,  0,  0,  0, 20, 20,
        -10,-20,-20,-20,-20,-20,-20,-10,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30]
}

# flip PST for black by mirroring indices
PST_B = {k.lower(): list(reversed(v)) for k, v in PST_W.items()}

DIRECTIONS = {
    'N': [-17,-15,-10,-6,6,10,15,17],
    'B': [-9,-7,7,9],
    'R': [-8,-1,1,8],
    'Q': [-9,-7,-8,-1,1,7,8,9],
    'K': [-9,-8,-7,-1,1,7,8,9]
}

@dataclass
class Move:
    from_sq: int
    to_sq: int
    piece: str
    capture: Optional[str] = None
    promotion: Optional[str] = None
    is_ep: bool = False
    is_castle: bool = False
    prev_castling: str = ''
    prev_ep: int = -1
    prev_halfmove: int = 0

class Board:
    def __init__(self):
        self.squares: List[str] = list(
            'rnbqkbnr'
            'pppppppp'
            '........'
            '........'
            '........'
            '........'
            'PPPPPPPP'
            'RNBQKBNR'
        )
        self.turn = WHITE
        self.castling = 'KQkq'
        self.ep_square = -1
        self.halfmove = 0
        self.fullmove = 1
        self.history: List[Move] = []

    def copy(self):
        b = Board()
        b.squares = self.squares.copy()
        b.turn = self.turn
        b.castling = self.castling
        b.ep_square = self.ep_square
        b.halfmove = self.halfmove
        b.fullmove = self.fullmove
        b.history = self.history.copy()
        return b

    def idx(self, file: int, rank: int) -> int:
        return rank*8 + file

    def fr(self, idx: int) -> Tuple[int,int]:
        return (idx % 8, idx // 8)

    def piece_at(self, idx: int) -> str:
        return self.squares[idx]

    def color_of(self, p: str) -> Optional[int]:
        if p == EMPTY: return None
        return WHITE if p.isupper() else BLACK

    def in_bounds(self, idx: int) -> bool:
        return 0 <= idx < 64

    def same_file(self, a: int, b: int) -> bool:
        return a % 8 == b % 8

    def same_rank(self, a: int, b: int) -> bool:
        return a // 8 == b // 8

    def algebraic(self, idx: int) -> str:
        f, r = self.fr(idx)
        return FILES[f] + RANKS[7-r]

    def king_square(self, color: int) -> int:
        target = 'K' if color==WHITE else 'k'
        return self.squares.index(target)

    def is_square_attacked(self, idx: int, by_color: int) -> bool:
        # Pawns
        f, r = self.fr(idx)
        if by_color == WHITE:
            caps = []
            if f>0 and r<7: caps.append(self.idx(f-1,r+1))
            if f<7 and r<7: caps.append(self.idx(f+1,r+1))
            for s in caps:
                if self.squares[s] == 'P':
                    return True
        else:
            caps = []
            if f>0 and r>0: caps.append(self.idx(f-1,r-1))
            if f<7 and r>0: caps.append(self.idx(f+1,r-1))
            for s in caps:
                if self.squares[s] == 'p':
                    return True
        # Knights
        for d in DIRECTIONS['N']:
            to = idx + d
            if not self.in_bounds(to):
                continue
            # ensure L-shape doesn't wrap files badly
            df = abs((to%8) - (idx%8))
            dr = abs((to//8) - (idx//8))
            if {df,dr}=={1,2}:
                p = self.squares[to]
                if p in ('N' if by_color==WHITE else 'n'):
                    return True
        # Bishops/Queens
        for d in DIRECTIONS['B']:
            to = idx + d
            while self.in_bounds(to) and abs((to%8)-( (to-d)%8))==1:
                p = self.squares[to]
                if p!=EMPTY:
                    if (p=='B' or p=='Q') and by_color==WHITE: return True
                    if (p=='b' or p=='q') and by_color==BLACK: return True
                    break
                to += d
        # Rooks/Queens
        for d in DIRECTIONS['R']:
            to = idx + d
            while self.in_bounds(to) and ( (d in (-1,1) and self.same_rank(to, to-d)) or (d in (-8,8)) ):
                p = self.squares[to]
                if p!=EMPTY:
                    if (p=='R' or p=='Q') and by_color==WHITE: return True
                    if (p=='r' or p=='q') and by_color==BLACK: return True
                    break
                to += d
        # Kings
        for d in DIRECTIONS['K']:
            to = idx + d
            if not self.in_bounds(to):
                continue
            if max(abs((to%8)-(idx%8)), abs((to//8)-(idx//8)))==1:
                p = self.squares[to]
                if p == ('K' if by_color==WHITE else 'k'):
                    return True
        return False

    def generate_pseudo_legal(self) -> List[Move]:
        moves: List[Move] = []
        color = self.turn
        for i, p in enumerate(self.squares):
            if p == EMPTY: continue
            if self.color_of(p) != color: continue
            if p.upper()=='P':
                self._gen_pawn_moves(i, p, moves)
            elif p.upper()=='N':
                for d in DIRECTIONS['N']:
                    to = i + d
                    if not self.in_bounds(to):
                        continue
                    df = abs((to%8)-(i%8)); dr = abs((to//8)-(i//8))
                    if {df,dr}!={1,2}: continue
                    t = self.squares[to]
                    if t==EMPTY or self.color_of(t)!=color:
                        moves.append(Move(i,to,p, capture=t if t!=EMPTY else None))
            elif p.upper() in ('B','R','Q'):
                dirs = DIRECTIONS['B'] if p.upper()=='B' else DIRECTIONS['R'] if p.upper()=='R' else DIRECTIONS['Q']
                for d in dirs:
                    to = i + d
                    while self.in_bounds(to) and ((d in (-1,1) and self.same_rank(to,to-d)) or (d in (-8,8)) or (d in (-9,-7,7,9) and abs((to%8)-((to-d)%8))==1)):
                        t = self.squares[to]
                        if t==EMPTY:
                            moves.append(Move(i,to,p))
                        else:
                            if self.color_of(t)!=color:
                                moves.append(Move(i,to,p,capture=t))
                            break
                        to += d
            elif p.upper()=='K':
                for d in DIRECTIONS['K']:
                    to = i + d
                    if not self.in_bounds(to): continue
                    if max(abs((to%8)-(i%8)), abs((to//8)-(i//8)))!=1: continue
                    t = self.squares[to]
                    if t==EMPTY or self.color_of(t)!=color:
                        moves.append(Move(i,to,p, capture=t if t!=EMPTY else None))
                # castling
                if (p=='K' and 'K' in self.castling) or (p=='k' and 'k' in self.castling):
                    if self.squares[i+1]==EMPTY and self.squares[i+2]==EMPTY:
                        if not self.is_square_attacked(i, 1-color) and not self.is_square_attacked(i+1,1-color) and not self.is_square_attacked(i+2,1-color):
                            moves.append(Move(i,i+2,p,is_castle=True))
                if (p=='K' and 'Q' in self.castling) or (p=='k' and 'q' in self.castling):
                    if self.squares[i-1]==EMPTY and self.squares[i-2]==EMPTY and self.squares[i-3]==EMPTY:
                        if not self.is_square_attacked(i, 1-color) and not self.is_square_attacked(i-1,1-color) and not self.is_square_attacked(i-2,1-color):
                            moves.append(Move(i,i-2,p,is_castle=True))
        return moves

    def _gen_pawn_moves(self, i: int, p: str, moves: List[Move]):
        color = WHITE if p.isupper() else BLACK
        dir = -8 if color==WHITE else 8
        rank = i//8
        to = i + dir
        if self.in_bounds(to) and self.squares[to]==EMPTY:
            if (color==WHITE and rank==1) or (color==BLACK and rank==6):
                # double push from start rank
                to2 = i + 2*dir
                if self.squares[to2]==EMPTY:
                    moves.append(Move(i,to2,p))
            # promotion?
            if (color==WHITE and to//8==0) or (color==BLACK and to//8==7):
                for promo in ('Q','R','B','N'):
                    moves.append(Move(i,to,p,promotion=promo if color==WHITE else promo.lower()))
            else:
                moves.append(Move(i,to,p))
        # captures
        for df in (-1,1):
            f = (i%8)+df
            if 0<=f<8:
                to = i + dir + df
                if not self.in_bounds(to): continue
                t = self.squares[to]
                if t!=EMPTY and self.color_of(t)!=color:
                    if (color==WHITE and to//8==0) or (color==BLACK and to//8==7):
                        for promo in ('Q','R','B','N'):
                            moves.append(Move(i,to,p,capture=t,promotion=promo if color==WHITE else promo.lower()))
                    else:
                        moves.append(Move(i,to,p,capture=t))
        # en passant
        if self.ep_square!=-1:
            ep = self.ep_square
            if abs((ep%8)-(i%8))==1 and ep//8 == (i//8) + (-1 if color==WHITE else 1):
                moves.append(Move(i,ep,p,is_ep=True))

    def legal_moves(self) -> List[Move]:
        res = []
        for m in self.generate_pseudo_legal():
            self.make_move(m)
            if not self.is_square_attacked(self.king_square(1-self.turn), self.turn):
                res.append(m)
            self.unmake_move()
        return res

    def make_move(self, m: Move):
        m.prev_castling = self.castling
        m.prev_ep = self.ep_square
        m.prev_halfmove = self.halfmove
        self.history.append(m)
        self.ep_square = -1
        piece = m.piece
        from_p = self.squares[m.from_sq]
        to_p = self.squares[m.to_sq]
        # halfmove clock
        if from_p.upper()=='P' or to_p!=EMPTY:
            self.halfmove = 0
        else:
            self.halfmove += 1
        # handle en passant capture
        if m.is_ep:
            if piece.isupper():
                cap_sq = m.to_sq + 8
            else:
                cap_sq = m.to_sq - 8
            m.capture = self.squares[cap_sq]
            self.squares[cap_sq] = EMPTY
        # move piece
        self.squares[m.to_sq] = self.squares[m.from_sq]
        self.squares[m.from_sq] = EMPTY
        # promotion
        if m.promotion:
            self.squares[m.to_sq] = m.promotion
        # castling move rook
        if m.is_castle:
            if m.to_sq > m.from_sq: # king side
                rook_from = m.from_sq+3
                rook_to = m.from_sq+1
            else: # queen side
                rook_from = m.from_sq-4
                rook_to = m.from_sq-1
            self.squares[rook_to] = self.squares[rook_from]
            self.squares[rook_from] = EMPTY
        # set en passant square for next move on double pawn push
        if piece.upper()=='P' and abs(m.to_sq - m.from_sq) == 16:
            self.ep_square = (m.to_sq + m.from_sq)//2
        else:
            self.ep_square = -1
        # update castling rights
        if piece=='K':
            self.castling = self.castling.replace('K','').replace('Q','')
        if piece=='k':
            self.castling = self.castling.replace('k','').replace('q','')
        if m.from_sq==63 or m.to_sq==63: # white h1 rook
            self.castling = self.castling.replace('K','')
        if m.from_sq==56 or m.to_sq==56: # white a1 rook
            self.castling = self.castling.replace('Q','')
        if m.from_sq==7 or m.to_sq==7:   # black h8 rook
            self.castling = self.castling.replace('k','')
        if m.from_sq==0 or m.to_sq==0:   # black a8 rook
            self.castling = self.castling.replace('q','')
        # switch turn and fullmove
        self.turn = 1 - self.turn
        if self.turn==WHITE:
            self.fullmove += 1

    def unmake_move(self):
        m = self.history.pop()
        self.turn = 1 - self.turn
        if self.turn==BLACK:
            self.fullmove -= 1
        self.castling = m.prev_castling
        self.ep_square = m.prev_ep
        self.halfmove = m.prev_halfmove
        # undo move
        piece = m.piece
        # undo castling rook
        if m.is_castle:
            if m.to_sq > m.from_sq:
                rook_from = m.from_sq+3
                rook_to = m.from_sq+1
            else:
                rook_from = m.from_sq-4
                rook_to = m.from_sq-1
            self.squares[rook_from] = self.squares[rook_to]
            self.squares[rook_to] = EMPTY
        # revert promotion
        moved_piece = piece
        self.squares[m.from_sq] = moved_piece
        self.squares[m.to_sq] = EMPTY if m.capture is None else m.capture
        if m.promotion:
            # original pawn
            self.squares[m.from_sq] = 'P' if piece.isupper() else 'p'
        # restore EP captured pawn
        if m.is_ep:
            if piece.isupper():
                cap_sq = m.to_sq + 8
                self.squares[cap_sq] = 'p'
            else:
                cap_sq = m.to_sq - 8
                self.squares[cap_sq] = 'P'
            self.squares[m.to_sq] = EMPTY

    def result(self) -> Optional[str]:
        legal = self.legal_moves()
        if legal:
            if self.halfmove >= 100:
                return '1/2-1/2'  # 50-move rule (100 halfmoves)
            return None
        # no legal moves
        if self.is_square_attacked(self.king_square(self.turn), 1-self.turn):
            return '1-0' if self.turn==BLACK else '0-1'
        else:
            return '1/2-1/2'  # stalemate

    def evaluate(self) -> int:
        score = 0
        for i,p in enumerate(self.squares):
            if p==EMPTY: continue
            score += VAL[p]
            if p.isupper():
                score += PST_W[p][i]
            else:
                score -= PST_B[p][i]
        # small mobility bonus
        mob = len(self.legal_moves())
        score += (5 if self.turn==WHITE else -5) * mob/20
        return int(score)

    def search(self, depth: int, alpha: int, beta: int) -> Tuple[int, Optional[Move]]:
        res = self.result()
        if res is not None:
            if res=='1-0': return (99999, None)
            if res=='0-1': return (-99999, None)
            return (0, None)
        if depth==0:
            return (self.evaluate(), None)
        best_move = None
        if self.turn==WHITE:
            max_eval = -10**9
            moves = self.legal_moves()
            # move ordering: captures first, then promotions
            moves.sort(key=lambda m: (m.capture is not None, m.promotion is not None), reverse=True)
            for m in moves:
                self.make_move(m)
                ev,_ = self.search(depth-1, alpha, beta)
                self.unmake_move()
                if ev>max_eval:
                    max_eval = ev
                    best_move = m
                alpha = max(alpha, ev)
                if beta <= alpha:
                    break
            return (max_eval, best_move)
        else:
            min_eval = 10**9
            moves = self.legal_moves()
            moves.sort(key=lambda m: (m.capture is not None, m.promotion is not None), reverse=True)
            for m in moves:
                self.make_move(m)
                ev,_ = self.search(depth-1, alpha, beta)
                self.unmake_move()
                if ev<min_eval:
                    min_eval = ev
                    best_move = m
                beta = min(beta, ev)
                if beta <= alpha:
                    break
            return (min_eval, best_move)

# ======================
# Pygame GUI
# ======================

CELL = 80
BOARD_SIZE = CELL*8
PANEL_W = 280
W, H = BOARD_SIZE + PANEL_W, BOARD_SIZE
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
HL_MOVE = (246, 246, 105)
HL_SEL = (106, 204, 110)
TEXT = (30,30,30)
BG = (250, 250, 250)
BTN = (230,230,230)
BTN_H = (210,210,210)

UNICODE_GLYPHS = {
    'K': '\u2654','Q': '\u2655','R': '\u2656','B': '\u2657','N': '\u2658','P': '\u2659',
    'k': '\u265A','q': '\u265B','r': '\u265C','b': '\u265D','n': '\u265E','p': '\u265F'
}

class ChessGUI:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Advanced Chess — Pygame')
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Segoe UI Symbol', 56)
        self.small = pygame.font.SysFont('Inter', 18)
        self.medium = pygame.font.SysFont('Inter', 22)
        self.board = Board()
        self.selected: Optional[int] = None
        self.legal_for_selected: List[Move] = []
        self.dragging = False
        self.drag_from: Optional[int] = None
        self.vs_ai = True
        self.ai_depth = 3
        self.move_list: List[str] = []

    def run(self):
        while True:
            self.handle_events()
            if self.vs_ai and self.board.turn==BLACK and self.selected is None and not self.dragging:
                # AI move
                _score, best = self.board.search(self.ai_depth, -10**9, 10**9)
                if best is None:
                    pass
                else:
                    self.board.make_move(best)
                    self.push_san(best)
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def push_san(self, m: Move):
        # very simple SAN-like text
        piece = m.piece.upper()
        san = '' if piece=='P' else piece
        if m.is_castle:
            san = 'O-O' if m.to_sq>m.from_sq else 'O-O-O'
        else:
            if m.capture:
                if piece=='P':
                    san = FILES[m.from_sq%8]
                san += 'x'
            san += self.board.algebraic(m.to_sq)
            if m.promotion:
                san += '=' + m.promotion.upper()
        res = self.board.result()
        if self.board.turn==WHITE:
            # just moved black
            self.move_list[-1] += ' ' + san
        else:
            self.move_list.append(f"{self.board.fullmove-1}. {san}")
        if res:
            self.move_list.append(res)

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_u:
                    self.undo()
                if e.key == pygame.K_r:
                    self.__init__()
                if e.key == pygame.K_a:
                    self.vs_ai = not self.vs_ai
                if e.key == pygame.K_1:
                    self.ai_depth = 1
                if e.key == pygame.K_2:
                    self.ai_depth = 2
                if e.key == pygame.K_3:
                    self.ai_depth = 3
                if e.key == pygame.K_4:
                    self.ai_depth = 4
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = e.pos
                if x<BOARD_SIZE:
                    sq = (y//CELL)*8 + (x//CELL)
                    self.select_square(sq)
                    self.dragging = True
                    self.drag_from = sq
                else:
                    self.panel_click(x,y)
            if e.type == pygame.MOUSEBUTTONUP:
                if self.dragging and self.drag_from is not None:
                    x,y = e.pos
                    if x<BOARD_SIZE:
                        to = (y//CELL)*8 + (x//CELL)
                        self.try_move(self.drag_from, to)
                self.dragging = False
                self.drag_from = None

    def undo(self):
        if not self.board.history:
            return
        self.board.unmake_move()
        if self.move_list:
            self.move_list.pop()
        if self.vs_ai and self.board.turn==BLACK and self.board.history:
            # undo one more to revert AI move as well
            self.board.unmake_move()
            if self.move_list:
                self.move_list.pop()

    def select_square(self, sq: int):
        p = self.board.piece_at(sq)
        if self.selected is None:
            if p!=EMPTY and self.board.color_of(p)==self.board.turn:
                self.selected = sq
                self.legal_for_selected = [m for m in self.board.legal_moves() if m.from_sq==sq]
        else:
            if sq==self.selected:
                self.selected = None
                self.legal_for_selected = []
            else:
                self.try_move(self.selected, sq)

    def try_move(self, fr: int, to: int):
        legal = [m for m in self.board.legal_moves() if m.from_sq==fr and m.to_sq==to]
        if not legal:
            # try promotion to queen by default if it's a promo square
            for m in self.board.legal_moves():
                if m.from_sq==fr and m.to_sq==to and m.promotion is not None:
                    legal = [m]
                    break
        if legal:
            m = legal[0]
            self.board.make_move(m)
            self.push_san(m)
        self.selected = None
        self.legal_for_selected = []

    def draw_board(self):
        for r in range(8):
            for f in range(8):
                x = f*CELL; y = r*CELL
                color = LIGHT if (r+f)%2==0 else DARK
                pygame.draw.rect(self.screen, color, (x,y,CELL,CELL))
        # highlights
        if self.selected is not None:
            sx = (self.selected%8)*CELL
            sy = (self.selected//8)*CELL
            pygame.draw.rect(self.screen, HL_SEL, (sx,sy,CELL,CELL), 6)
            for m in self.legal_for_selected:
                tx = (m.to_sq%8)*CELL; ty = (m.to_sq//8)*CELL
                pygame.draw.circle(self.screen, HL_MOVE, (tx+CELL//2, ty+CELL//2), 12)

    def draw_pieces(self):
        for i,p in enumerate(self.board.squares):
            if p==EMPTY: continue
            if self.dragging and self.drag_from==i:
                continue
            self.draw_piece_at(p, i)
        # draw dragging piece on top
        if self.dragging and self.drag_from is not None:
            p = self.board.squares[self.drag_from]
            if p!=EMPTY:
                mx,my = pygame.mouse.get_pos()
                if mx<BOARD_SIZE:
                    self.draw_glyph(p, mx-28, my-40)

    def draw_piece_at(self, p: str, idx: int):
        f = idx%8; r = idx//8
        x = f*CELL+ (CELL//2 - 24)
        y = r*CELL+ (CELL//2 - 28)
        self.draw_glyph(p, x, y)

    def draw_glyph(self, p: str, x: int, y: int):
        glyph = UNICODE_GLYPHS.get(p, p)
        try:
            surf = self.font.render(glyph, True, (0,0,0))
        except Exception:
            surf = self.font.render(p, True, (0,0,0))
        self.screen.blit(surf, (x,y))

    def panel_click(self, x:int, y:int):
        # buttons in side panel
        relx = x-BOARD_SIZE
        # Undo button
        if 20<=relx<=120 and 20<=y<=52:
            self.undo()
        # Reset
        if 140<=relx<=240 and 20<=y<=52:
            self.__init__()
        # Toggle AI
        if 20<=relx<=240 and 68<=y<=100:
            self.vs_ai = not self.vs_ai
        # Depth cycles
        if 20<=relx<=240 and 116<=y<=148:
            self.ai_depth = 1 + (self.ai_depth % 4)

    def draw_panel(self):
        x0 = BOARD_SIZE
        pygame.draw.rect(self.screen, BG, (x0,0,PANEL_W,H))
        # buttons
        self.button(x0+20, 20, 100, 32, 'Undo (U)')
        self.button(x0+140,20, 100, 32, 'Reset (R)')
        self.button(x0+20, 68, 220, 32, f"Play vs AI: {'ON' if self.vs_ai else 'OFF'} (A)")
        self.button(x0+20,116,220,32, f"AI Depth: {self.ai_depth}  (1-4 / click)")
        # move list
        self.label(x0+20, 170, 'Moves:')
        y = 196
        for line in self.move_list[-20:]:
            txt = self.small.render(line, True, TEXT)
            self.screen.blit(txt, (x0+20, y))
            y += 20
        # status
        res = self.board.result()
        turn_txt = 'White to move' if self.board.turn==WHITE else 'Black to move'
        if res:
            turn_txt = f"Game over: {res}"
        self.label(x0+20, H-40, turn_txt)

    def label(self, x:int, y:int, text:str):
        surf = self.medium.render(text, True, TEXT)
        self.screen.blit(surf, (x,y))

    def button(self, x:int, y:int, w:int, h:int, text:str):
        mx,my = pygame.mouse.get_pos()
        hovered = x<=mx<=x+w and y<=my<=y+h
        pygame.draw.rect(self.screen, BTN_H if hovered else BTN, (x,y,w,h), border_radius=8)
        pygame.draw.rect(self.screen, (200,200,200), (x,y,w,h), 1, border_radius=8)
        label = self.small.render(text, True, (20,20,20))
        self.screen.blit(label, (x+10, y+8))

    def draw_coords(self):
        # file letters & rank numbers3
        for f,ch in enumerate(FILES):
            txt = self.small.render(ch, True, (20,20,20))
            self.screen.blit(txt, (f*CELL+4, H-18))
        for r,ch in enumerate(reversed(RANKS)):
            txt = self.small.render(ch, True, (20,20,20))
            self.screen.blit(txt, (2, r*CELL+2))

    def draw(self):
        self.draw_board()
        self.draw_pieces()
        self.draw_coords()
        self.draw_panel()


if __name__ == '__main__':
    try:
        ChessGUI().run()
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit(0)
