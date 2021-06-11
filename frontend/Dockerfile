# ベースイメージの作成
FROM node:12.16.1-alpine
# ディレクトリの作成 （なくてもいい？）
RUN mkdir app
RUN mkdir app/frontend
# コンテナ内で作業するディレクトリを指定
WORKDIR /app/frontend/ragnarok
# package.json と package.lock を作業ディレクトリにコピー（ローカルからコンテナ内へ）
COPY ["./ragnarok/package.json", "./ragnarok/package-lock.json", "/app/frontend/ragnarok"]
# コンテナ内のnode_modules/.binにパスを通す
# ENV PATH /app/frontend/ragnarok/node_modules/.bin:$PATH
# RUN echo $PATH
# パッケージをインストール
RUN npm install
RUN npm install react-scripts
# ファイルをすべて作業用ディレクトリにコピー（ローカルからコンテナ内へ）
COPY . /app/frontend
# コンテナを起動する際に実行するコマンド
CMD [ "npm", "start" ]