-- CreateTable
CREATE TABLE "movie" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "releasedate" TEXT NOT NULL,
    "imageURL" TEXT,
    "description" TEXT,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "update_at" DATETIME NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "movie_id_key" ON "movie"("id");

-- CreateIndex
CREATE UNIQUE INDEX "movie_name_key" ON "movie"("name");
