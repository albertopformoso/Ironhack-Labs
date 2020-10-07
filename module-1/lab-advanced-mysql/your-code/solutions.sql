/*----------Challenge 1--------------*/
DROP TABLE IF EXISTS step_1;
DROP TABLE IF EXISTS step_2;
/*----------Step 1--------------*/
USE publications;
/*CREATE TEMPORARY TABLE step_1 AS */
SELECT titles.title_id 'TITLE ID', authors.au_id 'AUTHOR ID', (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) 'ROYALTY'
FROM titles
JOIN titleauthor
ON titles.title_id = titleauthor.title_id
JOIN sales
ON titles.title_id = sales.title_id
JOIN authors
ON titleauthor.au_id = authors.au_id
GROUP BY authors.au_id,titles.title_id;

/*----------Step 2--------------*/
 /*CREATE TEMPORARY TABLE step_2 AS*/
 SELECT step_2.title_id 'TITLE ID', step_2.au_id 'AUTHOR ID', SUM(ROYALTY) 'ROYALTIES'
 FROM (SELECT titles.title_id, authors.au_id, (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) 'ROYALTY'
	FROM titles
    JOIN titleauthor ON titles.title_id = titleauthor.title_id
    JOIN sales ON titles.title_id = sales.title_id
    JOIN authors ON titleauthor.au_id = authors.au_id
	) AS step_2
 GROUP BY step_2.au_id, step_2.title_id;
 
 /*----------Step 3--------------*/
 SELECT step_3.au_id 'AUTHOR ID', SUM(step_3.advance + ROYALTIES) 'PROFITS'
 FROM ( SELECT step_2.title_id, step_2.au_id, step_2.advance, SUM(ROYALTY) 'ROYALTIES'
	FROM ( SELECT titles.title_id, authors.au_id, titles.advance, (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) 'ROYALTY'
			FROM titles
			JOIN titleauthor ON titles.title_id = titleauthor.title_id
			JOIN sales ON titles.title_id = sales.title_id
			JOIN authors ON titleauthor.au_id = authors.au_id
        ) AS step_2
        GROUP BY au_id, title_id
    ) AS step_3
GROUP BY step_3.au_id
ORDER BY PROFITS DESC
LIMIT 3;
