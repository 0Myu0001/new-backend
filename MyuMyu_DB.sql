-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8mb4 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `user_id` VARCHAR(32) NOT NULL,
  `user_name` VARCHAR(32) NOT NULL,
  `user_image` BLOB NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_information` (
  `user_id` VARCHAR(32) NOT NULL,
  `user_email` VARCHAR(45) NOT NULL,
  `user_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_user_information_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user_follow`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_follow` (
  `user_id` VARCHAR(32) NOT NULL,
  `following_user_id` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `following_user_id_UNIQUE` (`following_user_id` ASC) VISIBLE,
  UNIQUE INDEX `user_user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_follow_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user_follower`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_follower` (
  `user_id` VARCHAR(32) NOT NULL,
  `followed_user_id` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `followed_user_id_UNIQUE` (`followed_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_follower_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music` (
  `music_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(32) NOT NULL,
  `music_title` VARCHAR(45) NOT NULL DEFAULT 'no title',
  `music_image` BLOB NOT NULL,
  `music` BLOB NOT NULL,
  `music_detail` LONGTEXT NULL,
  PRIMARY KEY (`music_id`),
  UNIQUE INDEX `idmusic_UNIQUE` (`music_id` ASC) VISIBLE,
  INDEX `fk_music_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_music_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_comments` (
  `user_id` VARCHAR(32) NOT NULL,
  `music_id` INT NOT NULL,
  `comment` LONGTEXT NOT NULL,
  PRIMARY KEY (`user_id`, `music_id`),
  INDEX `fk_user_has_music2_music1_idx` (`music_id` ASC) VISIBLE,
  INDEX `fk_user_has_music2_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_music2_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_music2_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist` (
  `playlist_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(32) NOT NULL,
  `playlist_title` VARCHAR(45) NOT NULL DEFAULT 'no title',
  `playlist_image` BLOB NOT NULL,
  `public` TINYINT NOT NULL DEFAULT 0,
  `playlist_detail` LONGTEXT NULL,
  PRIMARY KEY (`playlist_id`),
  UNIQUE INDEX `playlist_id_UNIQUE` (`playlist_id` ASC) VISIBLE,
  INDEX `fk_playlist_user1_idx` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_playlist_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist_music`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist_music` (
  `music_id` INT NOT NULL,
  `playlist_id` INT NOT NULL,
  PRIMARY KEY (`music_id`, `playlist_id`),
  INDEX `fk_music_has_playlist_playlist1_idx` (`playlist_id` ASC) VISIBLE,
  INDEX `fk_music_has_playlist_music1_idx` (`music_id` ASC) VISIBLE,
  CONSTRAINT `fk_music_has_playlist_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_music_has_playlist_playlist1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `mydb`.`playlist` (`playlist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist_music`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist_music` (
  `music_id` INT NOT NULL,
  `playlist_id` INT NOT NULL,
  PRIMARY KEY (`music_id`, `playlist_id`),
  INDEX `fk_music_has_playlist_playlist1_idx` (`playlist_id` ASC) VISIBLE,
  INDEX `fk_music_has_playlist_music1_idx` (`music_id` ASC) VISIBLE,
  CONSTRAINT `fk_music_has_playlist_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_music_has_playlist_playlist1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `mydb`.`playlist` (`playlist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_liked`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_liked` (
  `user_id` VARCHAR(32) NOT NULL,
  `music_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `music_id`),
  INDEX `fk_user_has_music1_music1_idx` (`music_id` ASC) VISIBLE,
  INDEX `fk_user_has_music1_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_music1_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_music1_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_contribute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_contribute` (
  `user_id` VARCHAR(32) NOT NULL,
  `music_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `music_id`),
  INDEX `fk_user_has_music_music1_idx` (`music_id` ASC) VISIBLE,
  INDEX `fk_user_has_music_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_music_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_music_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_tag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_tag` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist_liked`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist_liked` (
  `playlist_id` INT NOT NULL,
  `user_id` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`playlist_id`, `user_id`),
  INDEX `fk_playlist_has_user_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_playlist_has_user_playlist1_idx` (`playlist_id` ASC) VISIBLE,
  CONSTRAINT `fk_playlist_has_user_playlist1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `mydb`.`playlist` (`playlist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_playlist_has_user_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist_contribute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist_contribute` (
  `user_id` VARCHAR(32) NOT NULL,
  `playlist_id` INT NOT NULL,
  PRIMARY KEY (`playlist_id`, `user_id`),
  INDEX `fk_user_has_playlist_playlist1_idx` (`playlist_id` ASC) VISIBLE,
  INDEX `fk_user_has_playlist_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_playlist_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_playlist_playlist1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `mydb`.`playlist` (`playlist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist_liked`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist_liked` (
  `playlist_id` INT NOT NULL,
  `user_id` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`playlist_id`, `user_id`),
  INDEX `fk_playlist_has_user_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_playlist_has_user_playlist1_idx` (`playlist_id` ASC) VISIBLE,
  CONSTRAINT `fk_playlist_has_user_playlist1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `mydb`.`playlist` (`playlist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_playlist_has_user_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist_contribute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist_contribute` (
  `user_id` VARCHAR(32) NOT NULL,
  `playlist_id` INT NOT NULL,
  PRIMARY KEY (`playlist_id`, `user_id`),
  INDEX `fk_user_has_playlist_playlist1_idx` (`playlist_id` ASC) VISIBLE,
  INDEX `fk_user_has_playlist_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_playlist_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_playlist_playlist1`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `mydb`.`playlist` (`playlist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_contribute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_contribute` (
  `user_id` VARCHAR(32) NOT NULL,
  `music_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `music_id`),
  INDEX `fk_user_has_music_music1_idx` (`music_id` ASC) VISIBLE,
  INDEX `fk_user_has_music_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_music_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_music_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_liked`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_liked` (
  `user_id` VARCHAR(32) NOT NULL,
  `music_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `music_id`),
  INDEX `fk_user_has_music1_music1_idx` (`music_id` ASC) VISIBLE,
  INDEX `fk_user_has_music1_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_music1_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_music1_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`music_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`music_comments` (
  `user_id` VARCHAR(32) NOT NULL,
  `music_id` INT NOT NULL,
  `comment` LONGTEXT NOT NULL,
  PRIMARY KEY (`user_id`, `music_id`),
  INDEX `fk_user_has_music2_music1_idx` (`music_id` ASC) VISIBLE,
  INDEX `fk_user_has_music2_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_music2_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_music2_music1`
    FOREIGN KEY (`music_id`)
    REFERENCES `mydb`.`music` (`music_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `test` ;

-- -----------------------------------------------------
-- Table `test`.`api_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_user` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(25) NULL DEFAULT NULL,
  `user_name` VARCHAR(25) NULL DEFAULT NULL,
  `user_email` VARCHAR(254) NULL DEFAULT NULL,
  `follower_number` INT(11) NULL DEFAULT NULL,
  `following_number` INT(11) NULL DEFAULT NULL,
  `listened_number` INT(11) NULL DEFAULT NULL,
  `user_image` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `api_user_user_id_7d6e2bc5_uniq` (`user_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 150001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_notification`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_notification` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id_id` BIGINT(20) NOT NULL,
  `notification_id` VARCHAR(30) NULL DEFAULT NULL,
  `notification_content` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `api_notification_user_id_id_c8b9949c` (`user_id_id` ASC) VISIBLE,
  CONSTRAINT `api_notification_user_id_id_c8b9949c_fk_api_user_id`
    FOREIGN KEY (`user_id_id`)
    REFERENCES `test`.`api_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_playlist` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `playlist_id` VARCHAR(30) NULL DEFAULT NULL,
  `playlist_title` VARCHAR(30) NULL DEFAULT NULL,
  `playlist_image` VARCHAR(100) NULL DEFAULT NULL,
  `playlist_attributes` VARCHAR(1000) NULL DEFAULT NULL,
  `playlist_comment_number` INT(11) NULL DEFAULT NULL,
  `playlist_detail` VARCHAR(1000) NULL DEFAULT NULL,
  `playlist_loved_number` INT(11) NULL DEFAULT NULL,
  `playlist_played_times` INT(11) NULL DEFAULT NULL,
  `playlist_saved_number` INT(11) NULL DEFAULT NULL,
  `public` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `api_playlist_playlist_id_ef460cbe_uniq` (`playlist_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 30001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_playlist_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_playlist_comments` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `playlist_id` VARCHAR(30) NULL DEFAULT NULL,
  `comment_id` VARCHAR(30) NULL DEFAULT NULL,
  `comment_content` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_playlist_loved`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_playlist_loved` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `playlist_id` VARCHAR(30) NULL DEFAULT NULL,
  `loved_by_user_id` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_playlistposts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_playlistposts` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `playlist_id` VARCHAR(30) NOT NULL,
  `post_id` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `api_playlistposts_playlist_id_139bb902_fk_api_playlist_id` (`playlist_id` ASC) VISIBLE,
  INDEX `api_playlistposts_post_id_cacaf3bb_fk_api_post_id` (`post_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 180001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_post` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `post_id` VARCHAR(30) NULL DEFAULT NULL,
  `post_title` VARCHAR(30) NULL DEFAULT NULL,
  `post_image` VARCHAR(100) NULL DEFAULT NULL,
  `post_loved_number` INT(11) NULL DEFAULT NULL,
  `post_played_times` INT(11) NULL DEFAULT NULL,
  `post` VARCHAR(100) NULL DEFAULT NULL,
  `post_comment_number` INT(11) NULL DEFAULT NULL,
  `post_detail` VARCHAR(1000) NULL DEFAULT NULL,
  `post_saved_number` INT(11) NULL DEFAULT NULL,
  `post_tags` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `api_post_post_id_2c279d0b_uniq` (`post_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 150001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_post_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_post_comments` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `post_id` VARCHAR(30) NULL DEFAULT NULL,
  `comment_id` VARCHAR(30) NULL DEFAULT NULL,
  `comment_content` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_post_loved`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_post_loved` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `post_id` VARCHAR(30) NULL DEFAULT NULL,
  `loved_by_user_id` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`api_user_strict_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`api_user_strict_information` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(25) NULL DEFAULT NULL,
  `user_email` VARCHAR(254) NULL DEFAULT NULL,
  `user_phone_number` VARCHAR(30) NULL DEFAULT NULL,
  `user_password` VARCHAR(30) NULL DEFAULT NULL,
  `user_birth` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 60001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`auth_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`django_content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 180001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`auth_permission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT(11) NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC) VISIBLE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `test`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 180001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`auth_group_permissions` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `group_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `test`.`auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `test`.`auth_permission` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`auth_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(150) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 30001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`auth_user_groups` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `group_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC) VISIBLE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `test`.`auth_user` (`id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `test`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`auth_user_user_permissions` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `test`.`auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `test`.`auth_permission` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`authtoken_token`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`authtoken_token` (
  `key` VARCHAR(40) NOT NULL,
  `created` DATETIME(6) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE INDEX `user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `test`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`django_admin_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT(5) UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) VISIBLE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `test`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `test`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`django_migrations` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 450001
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`user_followers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user_followers` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `follower_id` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `test`.`user_followings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user_followings` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(30) NULL DEFAULT NULL,
  `following_id` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
