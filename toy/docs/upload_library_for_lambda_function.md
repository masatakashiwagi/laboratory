#　What's this?
- AWS Lambdaに使いたいライブラリをアップロードする方法

# How is that?
- 今回はpipを使用してrequestsをローカルディレクトリにインストールし，デプロイパッケージを作成する
    - 依存関係のディレクトリを作成
        - `~/$ mkdir package`
        - --targetオプションでライブラリをパッケージディレクトリにインストール
        - `~/$ cd package`
        - `~/package$ pip install requests --target .`
    - ZIPアーカイブの作成
        - `~/package$ zip -r9 ../function.zip .`
    - 関数コードをアーカイブに追加
        - `~/package$ cd ../`
        - `~/$ zip -g function.zip lambda_function.py`
    - ZIPアーカイブをlambdaにアップロード
        - lambdaの管理コンソールに移動し，「コード → アップロード元 →.zipファイルをアップロード」でZIPファイルをアップロードする

