CREATE TABLE "ltt_category_stage" (
  "id" varchar(64) NOT NULL,
  "name" varchar(128) NOT NULL,
  "user_id" int NOT NULL,
  "created" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id")
)