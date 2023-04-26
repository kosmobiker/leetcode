-- You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
-- Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

-- Root: If node is root node.
-- Leaf: If node is leaf node.
-- Inner: If node is neither root nor leaf node.

SELECT N, 
CASE
    WHEN P IS NULL THEN "Root"
    WHEN NOT EXISTS (SELECT inner_tbl.P FROM BST AS inner_tbl
                     WHERE inner_tbl.P = outer_tbl.N) THEN "Leaf"
    ELSE "Inner"
END
FROM BST AS outer_tbl
ORDER BY N ASC;