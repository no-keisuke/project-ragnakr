# ベースイメージの作成
FROM node:12.16.1
# ディレクトリの作成 （なくてもいい？）
RUN mkdir app
RUN mkdir app/frontend
# コンテナ内で作業するディレクトリを指定
WORKDIR /app/frontend/docker-practice
# package.json と package.lock を作業ディレクトリにコピー（ローカルからコンテナ内へ）
COPY ["./docker-practice/package.json", "./docker-practice/package-lock.json", "/app/frontend"]
# パッケージをインストール
RUN npm install
# ファイルをすべて作業用ディレクトリにコピー（ローカルからコンテナ内へ）
COPY . /app/frontend
# コンテナを起動する際に実行するコマンド（CMD との違いは万里の長城）
# CMD [ "/bin/bash" ]
CMD [ "npm", "start" ]