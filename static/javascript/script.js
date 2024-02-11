$(document).ready(function() {
    $('#submitWord').on('click', function() {
        var userWord = $('#userInput').val().trim();
        if (userWord) {
            // ユーザーの単語をサーバーに送信
            $.ajax({
                url: '/shiritori',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ user_word: userWord }),
                dataType: 'json',
                success: function(response) {
                    // CPUの応答を表示
                    $('#aiWord').text(response.cpu_word);
                    $('#status').text('次の単語を入力してください。');
                    // 入力フィールドをクリア
                    $('#userInput').val('');
                },
                error: function(xhr) {
                    // エラー処理
                    var errorMessage = xhr.responseJSON && xhr.responseJSON.message ? xhr.responseJSON.message : 'エラーが発生しました。';
                    $('#status').text(errorMessage);
                }
            });
        } else {
            // ユーザーが単語を入力していない場合
            $('#status').text('単語を入力してください。');
        }
    });

    // ゲームスタートボタンのイベントハンドラ
    $('#startGame').on('click', function() {
        // ゲームを開始するためのリクエストをサーバーに送信
        // スタートロジックは、サーバー側で定義される必要があります
    });

    // ゲーム終了ボタンのイベントハンドラ
    $('#endGame').on('click', function() {
        // ゲームを終了するためのリクエストをサーバーに送信
        // 終了ロジックは、サーバー側で定義される必要があります
    });
});
