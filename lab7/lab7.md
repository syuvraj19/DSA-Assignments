# Lab 7


* Yuvraj Singh
* Avreet Kaur
* Ravneet Kaur

## Part A: BST Insert

As a group review bst insertion algorithm.

![a98deb7e-e240-42a1-a9c3-f1f04d692a80](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/7c1c1562-f945-4eab-a81e-2ef4e09f4d0b)

* When completed, take one photo of the final tree

![3acca09b-5042-42ff-a906-a5ad973a2a7f](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/3497d0ae-74ea-431f-84a0-037d8eb9d611)

Answer this question.

* What is the height of your final tree?

6

## PART B: BST Deletion

* Find a node in your tree with 2 children and remove that node.
	* Take a picture of tree
![2103f03f-c8fa-41ef-90f9-fe8ae7b4a6d9](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/99717944-7e04-43bf-a86f-f8fa18ddddd9)

* find another node with 2 children and remove that node
	* Take picture of tree

![816a17ae-5c96-44b3-b1d9-5560f043e0fd](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/313d7b1e-733e-4a5d-8714-b7acbfafc48e)

* remove the root node of the tree
	* take picture of tree

![816a17ae-5c96-44b3-b1d9-5560f043e0fd](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/19f64562-b5f0-4ba1-9eb2-21ccc089e782)

Answer this question:

* Anytime you remove a node with 2 children, you need to find a node to take over for node being removed. Explain how you found your replacement.

To find a node to replace the node to be removed, I had to find the next biggest descendent and promote it to replace the removable node. For this, I proceeded with the right child of the removable node and then as far left as possible. 

## Part C AVL

* Take one photo of the original row of sticky notes

![a98deb7e-e240-42a1-a9c3-f1f04d692a80](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/c01811ae-98fa-4d29-a816-ecd52ae7ccbd)

* When completed, take one photo of the final tree

![a3864d6b-65b6-4ce3-ad3a-5649e88af4b6](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/7fcde42e-f4f8-4d9b-b971-b53748dc0d6d)


Answer these questions. 
* How many times you had to do a single rotation?
  
Four times

* How many times you had to do a double rotation?

once

* How tall is your final tree?

Height of final Tree is 6.

## Part D Red-black trees (optional)

* Take one photo of the original row of sticky notes

* When completed, take one photo of the final tree

* how many times did you perform a colour swap, zig-zig and zig-zag rotation?

## Part E 2-3 trees

* Take one photo of the original row of sticky notes

![a98deb7e-e240-42a1-a9c3-f1f04d692a80](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/336e1a8b-b659-4edf-9082-ba1c22b64eef)

* When completed, take one photo of the final tree

![090e5f7a-5453-462b-9e16-b6d877024c5b](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/d1c6e613-33f7-4e3f-9723-eac20a7b5ae2)

* How many times did you split?

6 Times

## Part F Dijkstra's Algorithm

![Graph](https://user-images.githubusercontent.com/1699186/203682880-1f8d6068-3668-4b2c-9abe-40cb79294177.png)


Use Dijkstra's algorithm to find the shortest distance from vertex A to every other vertex.  Show your work by creating the table below:

# Initial Table
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | FALSE |
| C      | ∞             |                 | FALSE |
| D      | ∞             |                 | FALSE |
| E      | ∞             |                 | FALSE |
| F      | 3             | A               | FALSE |
| G      | ∞             |                 | FALSE |

# Expanding E
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | FALSE |
| C      | 13            | F               | FALSE |
| D      | 12            | F               | FALSE |
| E      | 10            | F               | FALSE |
| F      | 3             | A               | TRUE  |
| G      | ∞             |                 | FALSE |

# Expanding B
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | TRUE  |
| C      | 9             | B               | FALSE |
| D      | 12            | F               | FALSE |
| E      | 10            | F               | FALSE |
| F      | 3             | A               | TRUE  |
| G      | ∞             |                 | FALSE |

# Expanding C
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | TRUE  |
| C      | 9             | B               | TRUE  |
| D      | 11            | C               | FALSE |
| E      | 10            | F               | FALSE |
| F      | 3             | A               | TRUE  |
| G      | ∞             |                 | FALSE |

# Expanding E
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | TRUE  |
| C      | 9             | B               | TRUE  |
| D      | 11            | C               | FALSE |
| E      | 10            | F               | TRUE  |
| F      | 3             | A               | TRUE  |
| G      | 15            | E               | FALSE |

# Expanding D
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | TRUE  |
| C      | 9             | B               | TRUE  |
| D      | 11            | C               | TRUE  |
| E      | 10            | F               | TRUE  |
| F      | 3             | A               | TRUE  |
| G      | 12            | D               | FALSE |

# Expanding G
| Vertex | Distance to A | Previous Vertex | Known |
|--------|---------------|-----------------|-------|
| A      | 0             |                 | TRUE  |
| B      | 5             | A               | TRUE  |
| C      | 9             | B               | TRUE  |
| D      | 11            | C               | TRUE  |
| E      | 10            | F               | TRUE  |
| F      | 3             | A               | TRUE  |
| G      | 12            | D               | TRUE |

Result summary: Fill in the final result in this table.  For path list all nodes for example, if you are going from A to B to C to D, then path is A-B-C-D

# FINAL TABLE
| Vertex | Path       | Distance to A |
|--------|------------|---------------|
| A      |            | 0             |
| B      | A-B        | 5             |
| C      | A-B-C      | 9             |
| D      | A-B-C-D    | 11            |
| E      | A-F-E      | 10            |
| F      | A-F        | 3             |
| G      | A-B-C-D-G  | 12            |

## Part G: Reflection

This lab taught me the importance of data structures and their practical applications. The exercises offered provide an in-depth understanding of how trees and graphs function, specifically how BSTs manage data, how AVL trees maintain balance, and how Dijkstra's algorithm can identify the shortest path in a weighted graph. The hands-on approach to problem-solving with these frameworks was beneficial, supplementing academic understanding with practical experience. This lab emphasised that, while the concepts can be difficult to grasp at first, with practice, they become more approachable and less daunting. It was very eye-opening to see these abstract concepts come to life in the form of pictures since it helped to consolidate my understanding of the topic.

