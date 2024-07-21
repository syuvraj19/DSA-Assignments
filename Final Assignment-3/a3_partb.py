# Main Author: Avreet Kaur
# Main Reviewer: Yuvraj Singh & Ravneet Kaur


from a3_parta import evaluate_board
from a1_partd import get_overflow_list, overflow
from a1_partc import Queue

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board

# Node class for the game tree
class Node:
    def __init__(self, board, depth, player, tree_height = 4):
        # A node should have a board representing the game at the time of the move is done
        self.board = board
        # Depth is to determine where it is min's or max's turn at the point where node reached
        self.depth = depth
        # Player is who played the node
        self.player = player
        # After the node is played, there are possible outcomes the opponent could play, which the references are stored in this array
        self.children = []
        # The score is to store the min or max of the children, which will add up to determine the end game score
        self.score = None
        # The move of the player at the time node is played
        self.move = None

# Game Tree class
class GameTree:
    def __init__(self, board, player, tree_height = 4):
        # Starting player at the initial phase
        self.player = player
        # Copy the whole board at the initial phase
        self.board = copy_board(board)
        # In the root node, the whole board should exist, depth should be 0, player selected should start
        self.root = Node(board, 0, player)
        # Height of the tree is predetermined
        self.tree_height = tree_height
        # Build the tree based on the given height and the root node
        self.build_tree(self.root, tree_height)

    # This function builds the game tree in the specified height
    # It accepts node as the root, and the height that limits the tree
    def build_tree(self, node, height):
        # No need to go further branching the tree if the predetermined height is reached
        if height == 0:
            return

        # It traverses the board at the time the node is played and finds the playable moves in the board
        for i in range(len(node.board)):
            for j in range(len(node.board[0])):
                # Find another potential branch that can be played
                if node.board[i][j] == 0 or node.board[i][j] * node.player > 0:
                    # Create a new board and add player's move to it
                    new_board = copy_board(node.board)
                    new_board[i][j] += node.player

                    # Perform overflow here if needed (get_overflow_list returns the number of the cells needs to be overflowes)
                    if get_overflow_list(new_board):
                            a_queue = Queue()
                            a_queue.enqueue(new_board)
                            overflow(new_board, a_queue)
                            new_board = a_queue.dequeue()
                            
                    # Child node will be played by the opposing player
                    child_node = Node(new_board, node.depth + 1, -node.player)
                    # Assign the move to each child that is born from that move
                    child_node.move = (i, j)
                    node.children.append(child_node)
                    
                    # Goes one depth deeper and continues to build the subtree with the child node
                    self.build_tree(child_node, height - 1)

    # This is a minimax function that returns the best score for the player and the worst score for the opponent for the subtree
    # It accepts node as the root of the subtree
    def minimax(self, node):
        if not node.children:
            # The function uses evaluate_board for calculating the score
            node.score = evaluate_board(node.board, node.player)
            return node.score
        
        # Maximizer is the player who starts from depth 0, and makes moves in 0, 2, and 4
        if node.depth % 2 == 0:  
            # Find the maximum score in maximizer turn
            node.score = max(self.minimax(child) for child in node.children)
            return node.score
        
        # Minimizer is the opponent who starts from depth 1, and makes moves in 1 and 3
        else:  
            # Find the minimum score in minimizer turn
            node.score = min(self.minimax(child) for child in node.children)
            return node.score

    # This function returns the best move in the board for the player
    def get_move(self):
        best_score = float('-inf')
        best_move = None
        # Search and find the best move in children with minimax algorithm
        for child in self.root.children:
            score = self.minimax(child)
            if score > best_score:
                best_score = score
                best_move = child.move
        return best_move
   
    # This function clears the nodes in the tree one by one
    def clear_tree(self):
         self.delete_nodes(self.root)
         
    # Helper function for deleting nodes one by one starting from the children
    # It accepts node as the root
    def delete_nodes(self, node):
        if not node:
            return
        for child in node.children:
            self.delete_nodes(child)
        del node

    


    
