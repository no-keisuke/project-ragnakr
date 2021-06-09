# ベースイメージの作成
FROM node:12.16.1
# コンテナ内で作業するディレクトリを指定
WORKDIR /frontend
# package.json と yarn.lock を作業ディレクトリにコピー（ローカルからコンテナ内へ）
COPY ["package.json", "yarn.lock", "./"]
# パッケージをインストール
RUN yarn install
# ファイルをすべて作業用ディレクトリにコピー（ローカルからコンテナ内へ）
COPY . .
# コンテナを起動する際に実行するコマンド（CMD との違いは万里の長城）
ENTRYPOINT [ "yarn", "start" ]