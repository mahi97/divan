.PHONY: help validate init-dry-run init

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

validate: ## Validate the template repo structure
	python tools/validate_template.py

init-dry-run: ## Dry-run project init (set TARGET, PROFILE, NAME, OWNER)
	python tools/init_project.py \
		--target $${TARGET:-../new_project} \
		--profile $${PROFILE:-base} \
		--project-name $${NAME:-new_project} \
		--owner $${OWNER:-myorg} \
		--dry-run

init: ## Initialize a sibling project (set TARGET, PROFILE, NAME, OWNER)
	python tools/init_project.py \
		--target $${TARGET:-../new_project} \
		--profile $${PROFILE:-base} \
		--project-name $${NAME:-new_project} \
		--owner $${OWNER:-myorg}
