# ベースイメージの作成
FROM node:12.16.1
# コンテナ内で作業するディレクトリを指定
WORKDIR /frontend
# package.json と package.lock を作業ディレクトリにコピー（ローカルからコンテナ内へ）
COPY ["package.json", "package.lock", "./"]
# パッケージをインストール
RUN npm install
# ファイルをすべて作業用ディレクトリにコピー（ローカルからコンテナ内へ）
COPY . .
# コンテナを起動する際に実行するコマンド（CMD との違いは万里の長城）
ENTRYPOINT [ "npm", "start" ]