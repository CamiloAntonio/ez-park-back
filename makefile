-include .env.make

connect:
	ssh -i $(SSH_KEY) -l $(SSH_USER) $(SERVER_IP)

prepare:
	ssh -i $(SSH_KEY) -l $(SSH_USER) $(SERVER_IP) "sudo apt-get update && sudo apt-get install -y docker.io docker-compose rsync"

deploy:
	rsync -avz --exclude '__pycache__' --exclude '.venv' --exclude 'ez-gcp' --exclude 'ez-gcp.pub' -e "ssh -i $(SSH_KEY)" ./ $(SSH_USER)@$(SERVER_IP):~/ez-park-back

ssh-up:
	ssh -i $(SSH_KEY) -l $(SSH_USER) $(SERVER_IP) "cd ~/ez-park-back && docker-compose up --build -d"

ssh-logs:
	ssh -i $(SSH_KEY) -l $(SSH_USER) $(SERVER_IP) "cd ~/ez-park-back && docker-compose logs -f"

ssh-stop:
	ssh -i $(SSH_KEY) -l $(SSH_USER) $(SERVER_IP) "cd ~/ez-park-back && docker-compose down"

gen-key:
	ssh-keygen -t rsa -b 4096 -f ~/.ssh/ez-gcp -N "" -C "$(USER)@$(HOSTNAME)"
	show-key

show-key:
	@echo "Copy and send this public key to the admin:"
	@cat ~/.ssh/ez-gcp.pub

dev:
	docker-compose up --build