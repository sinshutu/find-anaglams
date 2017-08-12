<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <meta charset="utf-8">
    <meta name="description" content="">
    <meta name="author" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- <link rel="shortcut icon" href=""> -->
  </head>
  <body>
    <form action="/create" method="POST">
      追加:
      <input type="text" name="text">
      <button type="submit">登録</button>
    </form>
    <h1>アナグラム一覧</h1>
    % for key, items in group.items():
    <hr>
    <ul>
      % for item in items:
      <li>{{item['text']}}</li>
      % end
    </ul>
    % end
  </body>
</html>
