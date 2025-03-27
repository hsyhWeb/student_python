/*
 Navicat Premium Dump SQL

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80404 (8.4.4)
 Source Host           : localhost:3306
 Source Schema         : student_scores

 Target Server Type    : MySQL
 Target Server Version : 80404 (8.4.4)
 File Encoding         : 65001

 Date: 27/03/2025 23:03:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for scores
-- ----------------------------
DROP TABLE IF EXISTS `scores`;
CREATE TABLE `scores`  (
  `姓名` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `总分` double NULL DEFAULT NULL,
  `班名` double NULL DEFAULT NULL,
  `级名` double NULL DEFAULT NULL,
  `语文` bigint NULL DEFAULT NULL,
  `语文级名` double NULL DEFAULT NULL,
  `数学` double NULL DEFAULT NULL,
  `数学级名` double NULL DEFAULT NULL,
  `英语` double NULL DEFAULT NULL,
  `英语级名` double NULL DEFAULT NULL,
  `物理` double NULL DEFAULT NULL,
  `物理级名` double NULL DEFAULT NULL,
  `化学` double NULL DEFAULT NULL,
  `化学级名` double NULL DEFAULT NULL,
  `生物` double NULL DEFAULT NULL,
  `生物级名` double NULL DEFAULT NULL,
  `考试名称` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of scores
-- ----------------------------
INSERT INTO `scores` VALUES ('陈思瀚', 598, 1, 6, 95, 318, 130, 1, 114, 96, 92, 5, 90, 32, 94, 1, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('安雪', 564, 2, 20, 106, 46, 114, 10, 126, 6, 77, 77, 81, 172, 86, 77, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('叶宇峰', 564.5, 3, 24, 90, 521, 126, 2, 102.5, 317, 88, 10, 90, 32, 88, 49, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('杨倩', 556.5, 4, 27, 100, 162, 116, 7, 121.5, 21, 73, 114, 84, 128, 88, 54, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('张铭宇', 557.5, 5, 28, 98, 218, 120, 3, 99.5, 392, 88, 10, 88, 53, 88, 54, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('陈果', 553, 6, 34, 90, 521, 118, 5, 124, 12, 75, 94, 82, 159, 89, 40, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('李晨昕', 544.5, 7, 55, 101, 135, 100, 21, 117.5, 54, 78, 67, 89, 43, 82, 145, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('邓程莹', 538, 8, 57, 111, 12, 116, 7, 121, 24, 65, 216, 70, 428, 84, 114, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('颜宾', 539, 9, 64, 100, 162, 113, 12, 103, 308, 80, 47, 81, 172, 88, 54, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('王佳畅', 537, 10, 70, 103, 86, 103, 18, 125, 9, 64, 231, 86, 83, 82, 145, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('黄贵华', 537.5, 11, 72, 98, 218, 114, 10, 109.5, 173, 79, 61, 85, 108, 77, 222, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('汪露', 532, 12, 79, 113, 6, 96, 28, 117, 61, 72, 124, 80, 206, 81, 175, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('李志杰', 518.5, 13, 110, 100, 162, 100, 21, 122.5, 18, 71, 135, 71, 400, 83, 135, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('周彦成', 518, 14, 118, 98, 218, 119, 4, 96, 464, 61, 286, 87, 67, 82, 145, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('曾陈婕', 514.5, 15, 129, 108, 25, 98, 25, 115.5, 74, 68, 177, 81, 172, 70, 387, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('苏爱凌', 508.5, 16, 151, 105, 62, 104, 17, 90.5, 542, 73, 114, 73, 340, 89, 35, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('卢世浩', 506, 17, 157, 98, 218, 101, 20, 103, 308, 67, 189, 80, 206, 84, 114, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('彭优祥', 503, 18, 171, 98, 218, 111, 14, 104, 281, 67, 189, 75, 303, 75, 272, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('戴庆沿', 500.5, 19, 178, 97, 250, 105, 16, 115.5, 74, 63, 250, 73, 340, 75, 272, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('陈维维', 496, 20, 192, 95, 318, 98, 25, 114, 96, 59, 316, 71, 400, 88, 54, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('康逍遥', 500, 20, 192, 95, 318, 99, 23, 101, 352, 71, 135, 85, 108, 74, 296, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('刘娇', 498.5, 22, 196, 101, 135, 113, 12, 87.5, 587, 71, 135, 78, 239, 74, 296, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('苏文', 497, 23, 206, 114, 4, 86, 32, 104, 281, 62, 269, 82, 159, 74, 296, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('蒲佳怡', 492, 24, 208, 103, 86, 86, 32, 138, 1, 43, 569, 67, 509, 84, 114, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('张晓霞', 495, 25, 213, 93, 407, 91, 31, 95, 477, 79, 61, 85, 108, 77, 222, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('邓杰', 488.5, 26, 227, 103, 86, 103, 18, 98.5, 410, 63, 250, 69, 451, 81, 175, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('尹洁', 489, 27, 230, 92, 444, 109, 15, 115, 80, 65, 216, 67, 509, 69, 405, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('马文家驹', 489.5, 28, 240, 103, 86, 83, 35, 80.5, 676, 78, 67, 82, 159, 88, 49, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('董鸿雁', 482.5, 29, 266, 105, 62, 97, 27, 98.5, 410, 63, 250, 70, 428, 77, 222, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('王宇欣', 478.5, 30, 278, 101, 135, 82, 37, 98.5, 410, 71, 135, 73, 340, 82, 145, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('孔储浩杰', 480, 31, 279, 98, 218, 118, 5, 88, 580, 63, 250, 76, 282, 64, 488, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('杨孟帆', 478.5, 32, 286, 88, 599, 116, 7, 86.5, 601, 65, 216, 77, 250, 73, 320, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('廖恒铭', 470.5, 33, 307, 100, 162, 95, 29, 102.5, 317, 72, 124, 62, 621, 68, 419, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('杨兆亿', 470.5, 34, 319, 95, 318, 82, 37, 119.5, 32, 54, 401, 73, 340, 74, 296, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('黄美娜', 467.5, 35, 333, 102, 111, 83, 35, 112.5, 112, 52, 430, 69, 451, 77, 222, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('黄欣蕊', 462.5, 36, 355, 97, 250, 81, 40, 106.5, 239, 63, 250, 70, 428, 73, 320, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('程羿然', 458, 37, 375, 56, 847, 99, 23, 120, 27, 67, 189, 70, 428, 74, 296, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('陈佳琪', 452.5, 38, 406, 95, 318, 92, 30, 98.5, 410, 52, 430, 77, 250, 64, 488, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('周丹丹', 448, 39, 417, 94, 355, 81, 40, 109, 180, 48, 493, 73, 340, 71, 361, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('王业胜', 440.5, 40, 463, 100, 162, 75, 43, 112.5, 112, 35, 686, 69, 451, 77, 222, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('杨鸿', 440, 41, 465, 94, 355, 82, 37, 93, 507, 65, 216, 67, 509, 67, 437, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('谢可欣', 399, 42, 650, 87, 636, 86, 32, 97, 445, 44, 555, 53, 764, 62, 522, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('马修婕', 385.5, 43, 685, 87, 636, 81, 40, 102.5, 317, 36, 676, 55, 744, 54, 589, '高三2班下期开学省联考成绩');
INSERT INTO `scores` VALUES ('平均分', 498.837209302326, NULL, NULL, 98, NULL, 100.511627906977, NULL, 107.116279069767, NULL, 66.0930232558139, NULL, 75.953488372093, NULL, 77.9302325581395, NULL, '高三2班下期开学省联考成绩');

SET FOREIGN_KEY_CHECKS = 1;
