/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80404 (8.4.4)
 Source Host           : localhost:3306
 Source Schema         : people

 Target Server Type    : MySQL
 Target Server Version : 80404 (8.4.4)
 File Encoding         : 65001

 Date: 16/04/2025 18:26:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` enum('male','female','other') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role` enum('student','teacher','admin') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` enum('active','disabled','pending') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT 'active',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, '嘿嘿', 'pass1234', 'male', 'admin', 'active');
INSERT INTO `users` VALUES (2, 'bob02', 'secure5678', 'male', 'teacher', 'active');
INSERT INTO `users` VALUES (3, 'charlie03', 'mypassword', 'other', 'admin', 'pending');
INSERT INTO `users` VALUES (4, 'diana04', 'abc123xyz', 'female', 'student', 'disabled');
INSERT INTO `users` VALUES (5, 'eric05', 'qwerty789', 'male', 'teacher', 'active');
INSERT INTO `users` VALUES (6, 'hsyh修改fsdfsdfsd', 'hsyh', 'male', 'teacher', 'active');
INSERT INTO `users` VALUES (7, 'hsy1h', 'hsyh', 'male', 'teacher', 'active');
INSERT INTO `users` VALUES (8, '123', '123', 'male', 'student', 'active');
INSERT INTO `users` VALUES (9, '456', '456', 'male', 'student', 'active');
INSERT INTO `users` VALUES (10, '777', '777', 'male', 'student', 'active');
INSERT INTO `users` VALUES (11, '111', '111', 'male', 'student', 'active');
INSERT INTO `users` VALUES (12, '10', '10', 'male', 'student', 'active');
INSERT INTO `users` VALUES (13, 'abc', 'abc', 'male', 'student', 'active');
INSERT INTO `users` VALUES (14, '888', '888', 'male', 'student', 'active');

SET FOREIGN_KEY_CHECKS = 1;
