# cli-chess
Chess cli game in python. 

Started 04/03

Implementation by order:
  - Piece class [X]
  - Chess board with unicode characters as pieces, with a print formating function [X]
  - FEN parsing function to set up board positions (which will also be used to update positions with new FEN) [X]
  - Adding castle, player turn and other parameters to FEN string []
  - Possible moves for each self.name __main__.Piece Object, function to subsidize moves from that function with any given FEN string []
  - PlayerPlay function, computerPlay function with legalMoves as an option []
  - Check, castle, en passant, 50 moves rules functions []
  - CheckDraw or CheckWin(param) functions (should include resign, draw agreement) []
  - Main event loop []
  
Once I finish this, the computer will only be able to play completely random moves. Then I can start to learn and implement machine learning
and make the computer play against itself.
