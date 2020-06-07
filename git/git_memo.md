## gitメモ
### commitのlogを確認する方法
```bash
git log --pretty=fuller
```

### repogitoryのAuthorを変更する
- localのusername/useremailを変更する
- 会社のアカウントで個人のrepogitoryにcommitしたくない時に変更すると良い
```bash
git config --local user.name "<username>"
git config --local user.email "<ID>+<username>@users.noreply.github.com"
```

### 過去のCommitのAuthorとCommitterを変更する方法
- 過去の全てのcommitについて変更したい場合，以下を実行する (AUthorとCommitterを変更する)
```bash
git filter-branch -f --env-filter \
  "GIT_AUTHOR_NAME='<username>'; \
   GIT_AUTHOR_EMAIL='<ID>+<username>@users.noreply.github.com'; \
   GIT_COMMITTER_NAME='<username>'; \
   GIT_COMMITTER_EMAIL='<ID>+<username>@users.noreply.github.com';" \
  HEAD
```

- 特定条件のcommitのみ修正したい場合は，次のように条件を追記する
```bash
git filter-branch --commit-filter ' 
  if [ "$GIT_COMMITTER_EMAIL" = "example@example.com" ];
    then
        GIT_COMMITTER_NAME="example";
        GIT_AUTHOR_NAME="example";
        GIT_COMMITTER_EMAIL="example@example.com";
        GIT_AUTHOR_EMAIL="example@example.com";
        git commit-tree "$@";
    else
        git commit-tree "$@";
    fi'  HEAD
```

### remote repogitoryにpushした際に，reject errorとなった場合の対応法
```bash
git merge --allow-unrelated-histories origin/master
```
- `--allow-unrelated-histories`について

Git 2.9からmergeコマンドとpullコマンドでは，`--allow-unrelated-histories`を指定しない限り，無関係なヒストリを持つ２つのブランチをマージすることはできなくなった
