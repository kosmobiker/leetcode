-- You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
-- Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

-- Root: If node is root node.
-- Leaf: If node is leaf node.
-- Inner: If node is neither root nor leaf node.

SELECT
    N,
    CASE
        WHEN P IS NULL THEN "Root"
        WHEN NOT EXISTS (
            SELECT INNER_TBL.P FROM BST AS INNER_TBL
            WHERE INNER_TBL.P = OUTER_TBL.N
        ) THEN "Leaf"
        ELSE "Inner"
    END
FROM BST AS OUTER_TBL
ORDER BY N ASC;
