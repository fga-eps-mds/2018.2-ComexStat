run-docs:
	docker pull vinicinolivera/gh-pages-docker-travis
docker run --rm -p 3000:3000 -p 35729:35729 -v `pwd`:"/app" -w "/app" -it vinicinolivera/gh-pages-docker-travis bash -c "cd website; yarn install; yarn run start"
