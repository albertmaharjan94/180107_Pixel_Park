-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2020 at 03:26 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pixel_park`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user', 1, 'add_user'),
(2, 'Can change user', 1, 'change_user'),
(3, 'Can delete user', 1, 'delete_user'),
(4, 'Can view user', 1, 'view_user'),
(5, 'Can add post', 2, 'add_post'),
(6, 'Can change post', 2, 'change_post'),
(7, 'Can delete post', 2, 'delete_post'),
(8, 'Can view post', 2, 'view_post'),
(9, 'Can add photo', 3, 'add_photo'),
(10, 'Can change photo', 3, 'change_photo'),
(11, 'Can delete photo', 3, 'delete_photo'),
(12, 'Can view photo', 3, 'view_photo'),
(13, 'Can add like', 4, 'add_like'),
(14, 'Can change like', 4, 'change_like'),
(15, 'Can delete like', 4, 'delete_like'),
(16, 'Can view like', 4, 'view_like'),
(17, 'Can add follow', 5, 'add_follow'),
(18, 'Can change follow', 5, 'change_follow'),
(19, 'Can delete follow', 5, 'delete_follow'),
(20, 'Can view follow', 5, 'view_follow'),
(21, 'Can add comment', 6, 'add_comment'),
(22, 'Can change comment', 6, 'change_comment'),
(23, 'Can delete comment', 6, 'delete_comment'),
(24, 'Can view comment', 6, 'view_comment'),
(25, 'Can add log entry', 7, 'add_logentry'),
(26, 'Can change log entry', 7, 'change_logentry'),
(27, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can view log entry', 7, 'view_logentry'),
(29, 'Can add permission', 8, 'add_permission'),
(30, 'Can change permission', 8, 'change_permission'),
(31, 'Can delete permission', 8, 'delete_permission'),
(32, 'Can view permission', 8, 'view_permission'),
(33, 'Can add group', 9, 'add_group'),
(34, 'Can change group', 9, 'change_group'),
(35, 'Can delete group', 9, 'delete_group'),
(36, 'Can view group', 9, 'view_group'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add content type', 11, 'add_contenttype'),
(42, 'Can change content type', 11, 'change_contenttype'),
(43, 'Can delete content type', 11, 'delete_contenttype'),
(44, 'Can view content type', 11, 'view_contenttype'),
(45, 'Can add session', 12, 'add_session'),
(46, 'Can change session', 12, 'change_session'),
(47, 'Can delete session', 12, 'delete_session'),
(48, 'Can view session', 12, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `title` varchar(191) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `title`, `status`, `date`, `post_id`, `user_id`) VALUES
(1, 'You look cute, You inspire me.', 0, '2020-02-15 14:48:38.478857', 2, 5),
(2, 'Idols', 0, '2020-02-15 14:54:17.609452', 4, 6),
(5, 'you\'re my idol <3', 0, '2020-02-15 15:09:06.842296', 12, 2),
(7, 'nice hair billie', 0, '2020-02-15 23:57:20.092416', 20, 5);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(9, 'auth', 'group'),
(8, 'auth', 'permission'),
(10, 'auth', 'user'),
(11, 'contenttypes', 'contenttype'),
(6, 'pixel_park_django', 'comment'),
(5, 'pixel_park_django', 'follow'),
(4, 'pixel_park_django', 'like'),
(3, 'pixel_park_django', 'photo'),
(2, 'pixel_park_django', 'post'),
(1, 'pixel_park_django', 'user'),
(12, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-02-15 08:49:50.580924'),
(2, 'auth', '0001_initial', '2020-02-15 08:49:50.768951'),
(3, 'admin', '0001_initial', '2020-02-15 08:49:51.362000'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-02-15 08:49:51.535458'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-02-15 08:49:51.545400'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-02-15 08:49:51.619476'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-02-15 08:49:51.678657'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-02-15 08:49:51.693618'),
(9, 'auth', '0004_alter_user_username_opts', '2020-02-15 08:49:51.701596'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-02-15 08:49:51.753458'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-02-15 08:49:51.756475'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-02-15 08:49:51.764449'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-02-15 08:49:51.778392'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-02-15 08:49:51.796343'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-02-15 08:49:51.813299'),
(16, 'auth', '0011_update_proxy_permissions', '2020-02-15 08:49:51.822275'),
(17, 'pixel_park_django', '0001_initial', '2020-02-15 08:49:52.012764'),
(18, 'sessions', '0001_initial', '2020-02-15 08:49:52.539357');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7u7sse573sg051vtbg5a2d9zcylccev9', 'MzkzNmIzNTRhZWIwMjMzNGUxOTE1NTZlMGVmZDk1NWZiNjI0Yzk5Zjp7InVzZXIiOjF9', '2020-03-01 10:41:01.532129'),
('aeaswkpv13m1ett5zmc33onqqsn7ps7k', 'N2U2ZGI1ZGVhNDFkZTk3MDQ5ZGEzYTJlOGFmNmRjNjdmNjZhYzg5Mzp7InVzZXIiOjJ9', '2020-03-01 09:28:49.827211'),
('xii2m0ntj35ifflt31soc5mri3v7oc5v', 'N2U2ZGI1ZGVhNDFkZTk3MDQ5ZGEzYTJlOGFmNmRjNjdmNjZhYzg5Mzp7InVzZXIiOjJ9', '2020-02-29 09:23:30.357628');

-- --------------------------------------------------------

--
-- Table structure for table `follows`
--

CREATE TABLE `follows` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `follower_id` int(11) NOT NULL,
  `following_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `follows`
--

INSERT INTO `follows` (`id`, `status`, `date`, `follower_id`, `following_id`) VALUES
(1, 0, '2020-02-15 14:43:23.714992', 3, 2),
(2, 0, '2020-02-15 14:45:33.865068', 4, 3),
(3, 0, '2020-02-15 14:45:34.570178', 4, 2),
(4, 0, '2020-02-15 14:48:20.474492', 5, 4),
(5, 0, '2020-02-15 14:48:21.107250', 5, 3),
(7, 0, '2020-02-15 14:53:48.241481', 6, 5),
(8, 0, '2020-02-15 14:53:52.438279', 6, 2),
(9, 0, '2020-02-15 14:57:31.382079', 7, 5),
(10, 0, '2020-02-15 14:57:32.623447', 7, 2),
(11, 0, '2020-02-15 14:59:34.521966', 8, 5),
(12, 0, '2020-02-15 14:59:39.609361', 8, 2),
(13, 0, '2020-02-15 15:02:08.772016', 8, 7),
(14, 0, '2020-02-15 15:02:11.035195', 8, 4),
(19, 0, '2020-02-15 15:08:49.258405', 2, 7),
(21, 0, '2020-02-15 20:26:43.296679', 2, 5),
(22, 0, '2020-02-15 20:26:49.955812', 2, 6),
(23, 0, '2020-02-15 23:57:10.374228', 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `likes`
--

INSERT INTO `likes` (`id`, `status`, `date`, `post_id`, `user_id`) VALUES
(1, 0, '2020-02-15 14:44:06.671372', 3, 3),
(2, 0, '2020-02-15 14:44:09.863678', 2, 3),
(4, 0, '2020-02-15 14:47:20.225537', 2, 4),
(5, 0, '2020-02-15 14:47:26.512068', 3, 4),
(6, 0, '2020-02-15 14:48:26.438877', 2, 5),
(7, 0, '2020-02-15 14:48:28.357957', 3, 5),
(8, 0, '2020-02-15 14:53:49.963291', 12, 6),
(9, 0, '2020-02-15 14:53:51.305782', 11, 6),
(10, 0, '2020-02-15 14:53:56.217895', 3, 6),
(11, 0, '2020-02-15 14:53:59.002738', 2, 6),
(12, 0, '2020-02-15 14:54:07.918693', 4, 6),
(13, 0, '2020-02-15 14:57:34.677137', 12, 7),
(14, 0, '2020-02-15 14:57:39.088618', 2, 7),
(15, 0, '2020-02-15 14:57:40.360947', 3, 7),
(16, 0, '2020-02-15 14:59:37.322558', 12, 8),
(17, 0, '2020-02-15 14:59:38.431504', 11, 8),
(18, 0, '2020-02-15 14:59:43.708313', 2, 8),
(19, 0, '2020-02-15 15:02:13.816694', 16, 8),
(25, 0, '2020-02-15 15:08:54.890874', 16, 2),
(26, 0, '2020-02-15 15:08:56.689023', 15, 2),
(27, 0, '2020-02-15 15:08:59.511798', 12, 2),
(28, 0, '2020-02-15 15:09:01.015866', 11, 2),
(29, 0, '2020-02-15 23:57:15.432848', 20, 5);

-- --------------------------------------------------------

--
-- Table structure for table `photos`
--

CREATE TABLE `photos` (
  `id` int(11) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `post_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `photos`
--

INSERT INTO `photos` (`id`, `photo`, `status`, `post_id`) VALUES
(3, '1581756894.png', 0, 3),
(4, '1581757082.png', 0, 4),
(5, '1581757101.png', 0, 5),
(6, '1581757127.png', 0, 6),
(7, '1581757252.png', 0, 7),
(8, '1581757274.png', 0, 8),
(9, '1581757291.png', 0, 9),
(10, '1581757449.png', 0, 10),
(11, '1581757470.png', 0, 11),
(12, '1581757522.png', 0, 12),
(13, '1581757782.png', 0, 13),
(14, '1581757817.png', 0, 14),
(15, '1581757948.png', 0, 15),
(16, '1581757997.png', 0, 16),
(17, '1581758111.png', 0, 17),
(20, '1581783315.png', 0, 20),
(30, '1581838942.jpg', 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `caption` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `caption`, `status`, `date`, `user_id`) VALUES
(2, 'Have you watched my new music video ', 0, '2020-02-15 14:38:52.229576', 2),
(3, 'I showd up on #billboard ', 0, '2020-02-15 14:39:54.892588', 2),
(4, 'With Robert Plant #LedZeppelin', 0, '2020-02-15 14:43:02.261071', 3),
(5, 'B&W', 0, '2020-02-15 14:43:21.273291', 3),
(6, 'Check out my biography', 0, '2020-02-15 14:43:47.401191', 3),
(7, 'California #concert', 0, '2020-02-15 14:45:52.540419', 4),
(8, 'Did photoshoot at #Gucci', 0, '2020-02-15 14:46:14.136261', 4),
(9, 'Deep Thinking #maroon5', 0, '2020-02-15 14:46:31.076300', 4),
(10, 'Orange Microphone #paramore', 0, '2020-02-15 14:49:09.791575', 5),
(11, 'Love you all #paramorefam', 0, '2020-02-15 14:49:30.549048', 5),
(12, 'Orange Hair anytime #paramore', 0, '2020-02-15 14:50:22.682374', 5),
(13, 'Store Sour ', 0, '2020-02-15 14:54:42.996398', 6),
(14, 'If you love me let me go. Snuff #slipknot', 0, '2020-02-15 14:55:17.264159', 6),
(15, 'Short Hair', 0, '2020-02-15 14:57:28.087014', 7),
(16, 'Going old school', 0, '2020-02-15 14:58:17.778582', 7),
(17, '<3 from my heart', 0, '2020-02-15 15:00:11.782452', 8),
(20, 'green hair #green', 0, '2020-02-15 22:00:15.985534', 2);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(240) NOT NULL,
  `password` varchar(191) NOT NULL,
  `social_link` longtext NOT NULL,
  `is_admin` int(11) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `email`, `password`, `social_link`, `is_admin`, `image`) VALUES
(1, 'Admin', 'admin', 'admin@admin.com', 'pbkdf2_sha256$180000$11jvtiiUKBHC$auc9CWxTbuR3QXiLor6fLeY5hO9RPqELpuC2uQJQ1Vs=', '', 1, 'user.png'),
(2, 'Billie Eilish', 'billie_e', 'billie@gmail.com', 'pbkdf2_sha256$180000$qR6g5dUeyKHB$ZR8yaDHyaZfAtj6cI767+EdHAXZODZN9sw+Xv84F368=', '', 0, '1581756900.jpg'),
(3, 'Jimmy Page', 'jimmy.page', 'jimmypage@gmail.com', 'pbkdf2_sha256$180000$2UL6ZvhTMEaj$svuG/8R1hCfkJKFmMaQ7Pi+QuBfuQTCAsMRAkuaQo1k=', '', 0, '1581757134.jpg'),
(4, 'Adam Levine', 'adam.levine2k', 'adamlevine@gmail.com', 'pbkdf2_sha256$180000$jhYobo6MfMJ1$YHTYDl3DFeHB8Z2q5B5ikseVUYx2PAbulI1fuzJZ9NI=', '', 0, '1581757313.jpg'),
(5, 'Hayley William', 'hayley.williams123', 'hayley@gmail.com', 'pbkdf2_sha256$180000$Io2zeJlXHY1m$c79rP8BdqmjmtxG648NQgcQ+bHIzl/pwg0AQDlIN80Q=', 'http://youtube.com/haley', 0, '1581757570.webp'),
(6, 'Corey Taylor', 'corey.taylor', 'corey@gmail.com', 'pbkdf2_sha256$180000$H9z4nXsnAmkn$JadnkhV5FTNGDFTv70B7SAe6IXNsq1EHHtwlczATRo0=', '', 0, '1581757769.jpg'),
(7, 'Katy Perry', 'katy.perry', 'katy@gmail.com', 'pbkdf2_sha256$180000$fdeTiyYgLeb9$F6RbnKPiPadD6NjawxSa4RXz7+DnUns3Z87r8WTZvA0=', '', 0, '1581757933.jpg'),
(8, 'Taylor Swift', 'taylor.swift', 'taylor@gmail.com', 'pbkdf2_sha256$180000$JtAa5rxuJIpB$26bh4LarThSmyudJZbzwN4ctExeC9jQLcnwVI8nebp8=', '', 0, '1581758096.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `comments_post_id_67cfce36_fk_posts_id` (`post_id`),
  ADD KEY `comments_user_id_b8fd0b64_fk_users_id` (`user_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `follows`
--
ALTER TABLE `follows`
  ADD PRIMARY KEY (`id`),
  ADD KEY `follows_follower_id_63fa6a23_fk_users_id` (`follower_id`),
  ADD KEY `follows_following_id_0427f0f6_fk_users_id` (`following_id`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `likes_post_id_84cc5834_fk_posts_id` (`post_id`),
  ADD KEY `likes_user_id_0899754c_fk_users_id` (`user_id`);

--
-- Indexes for table `photos`
--
ALTER TABLE `photos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `photos_post_id_caa37f85_fk_posts_id` (`post_id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `posts_user_id_4291758d_fk_users_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `follows`
--
ALTER TABLE `follows`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `likes`
--
ALTER TABLE `likes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `photos`
--
ALTER TABLE `photos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_post_id_67cfce36_fk_posts_id` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`),
  ADD CONSTRAINT `comments_user_id_b8fd0b64_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `follows`
--
ALTER TABLE `follows`
  ADD CONSTRAINT `follows_follower_id_63fa6a23_fk_users_id` FOREIGN KEY (`follower_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `follows_following_id_0427f0f6_fk_users_id` FOREIGN KEY (`following_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `likes`
--
ALTER TABLE `likes`
  ADD CONSTRAINT `likes_post_id_84cc5834_fk_posts_id` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`),
  ADD CONSTRAINT `likes_user_id_0899754c_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `photos`
--
ALTER TABLE `photos`
  ADD CONSTRAINT `photos_post_id_caa37f85_fk_posts_id` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`);

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_user_id_4291758d_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
