# Default settings
ELASTIC_PORT ?= 9200
OLLAMA_PORT ?= 11434
POSTGRES_PORT ?= 5432
STREAMLIT_PORT ?= 8501
GRAFANA_ADMIN_PASSWORD ?= admin

# Service names
SERVICES = elasticsearch ollama postgres streamlit grafana

# Helper commands
up_service = docker compose up -d $(1)
down_service = docker compose stop $(1) && docker compose rm -f $(1)
rebuild_service = $(call down_service,$(1)) && docker compose build $(1) && $(call up_service,$(1))
destroy_service = docker compose stop $(1) && docker compose rm -f $(1) && docker volume rm -f $($(1)_data)

# Individual service commands
define generate_service_commands
.PHONY: $(1)_up $(1)_down $(1)_rebuild $(1)_destroy
$(1)_up:
	$(call up_service,$(1))

$(1)_down:
	$(call down_service,$(1))

$(1)_rebuild:
	$(call rebuild_service,$(1))

$(1)_destroy:
	$(call destroy_service,$(1))
endef

$(foreach service,$(SERVICES),$(eval $(call generate_service_commands,$(service))))

# General commands
.PHONY: up down rebuild destroy
up:
	docker compose up -d

down:
	docker compose down

rebuild:
	docker compose down && docker compose build && docker compose up -d

destroy:
	docker compose down -v && docker volume prune -f
