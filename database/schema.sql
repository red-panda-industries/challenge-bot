CREATE TABLE IF NOT EXISTS `blacklist` (
  `user_id` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `warns` (
  `id` int(11) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `server_id` varchar(20) NOT NULL,
  `moderator_id` varchar(20) NOT NULL,
  `reason` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `activity` (
  `id` int(11) NOT NULL
    CONSTRAINT activity_pk PRIMARY KEY AUTOINCREMENT,
  `user_id` varchar(20) NOT NULL
    INDEX activity_user_id_idx,
  `type` varchar(20) NOT NULL
    INDEX activity_type_idx,
  `created_at` timestamp NOT NULL
    INDEX activity_created_at_idx
    DEFAULT CURRENT_TIMESTAMP
);