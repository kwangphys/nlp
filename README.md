# NLP Analysis for News Articles
This package aims to use nlp tools to extract and quantify numeric information from news articles. This is an ongoing progress and the idea to attack this problem takes following steps:
  1. Filter out sentences which contain numeric information.
  2. Shorten these sentences by only keeping subject/verb/object/numeric group/time/other necessary words
  3. Map shortened sentences to a few possible language structures and find each word part
  4. Process each part of the shortened sentence:
      - Recognize entities for subjects and objects, and normalize their name, e.g. to stock tickers
      - Classify verbs to a group of possible actions, e.g. be, increase, reduce etc
      - Analyze numeric group to identify the number, unit and possible adverbials such as about, more than, etc
      - Normalize time information into datetime
  5. Integrate above analysis and save them as structured data, possibly a database table
