-- phpMyAdmin SQL Dump
-- version 5.2.1deb1ubuntu0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 27, 2024 at 12:55 PM
-- Server version: 8.0.35-0ubuntu0.23.04.1
-- PHP Version: 8.1.12-1ubuntu4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `CandyStore`
--

-- --------------------------------------------------------

--
-- Table structure for table `candy`
--

CREATE TABLE `candy` (
  `candy_id` int NOT NULL COMMENT 'Unique Identifier',
  `category_ids` json NOT NULL COMMENT 'List of integer Ids of \r\n each category candy is in',
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Name of the candy',
  `description` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Describes the candy',
  `price` float NOT NULL COMMENT 'price of the candy',
  `image_paths` json NOT NULL COMMENT 'list of paths to various size  images of the candy'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `candy`
--

INSERT INTO `candy` (`candy_id`, `category_ids`, `name`, `description`, `price`, `image_paths`) VALUES
(0, '[0, 15, 33]', 'Gourmet Salt Water Taffy - Bulk', 'No one can resist the smooth texture and mouthwatering flavor of classic saltwater taffy! This nostalgic delight emerged from Atlantic City, NJ to become one of the most popular confections in the world. Often used in wedding favors or given as a special gift, saltwater taffy is sure to please any sweet tooth! Each individually wrapped piece includes rich molasses, sea salt and palm oil to produce that creamy taste experience that has everyone reaching for a second piece, or even a third and fourth!Saltwater taffy comes in a long list of delicious flavors, each featuring its own unique color. The many pastel hues, like yellow, pink and orange, harken back to this candy\'s seaside origins. You\'ll love sampling each distinct flavor, like caramel swirl or root beer float! Nothings better than a stroll along the boardwalk with watermelon or raspberry saltwater taffy. Explore our flavor list today and discover your new favorite beach snack!\r\n\r\nChoose from over 60 different flavors or mixes. When all flavors and mixes are available, there are more than 60 to choose from. The Assorted Taffy mix contains about 15 flavors.', 19.99, '[\"./images_sized/kosher-candy/0_64.jpg\", \"./images_sized/kosher-candy/0_96.jpg\", \"./images_sized/kosher-candy/0_128.jpg\", \"./images_sized/kosher-candy/0_256.jpg\", \"./images_sized/kosher-candy/0_512.jpg\", \"./images_sized/kosher-candy/0_768.jpg\", \"./images_sized/salt-water-taffy/0_64.jpg\", \"./images_sized/salt-water-taffy/0_96.jpg\", \"./images_sized/salt-water-taffy/0_128.jpg\", \"./images_sized/salt-water-taffy/0_256.jpg\", \"./images_sized/salt-water-taffy/0_512.jpg\", \"./images_sized/salt-water-taffy/0_768.jpg\", \"./images_sized/soft-candy/0_64.jpg\", \"./images_sized/soft-candy/0_96.jpg\", \"./images_sized/soft-candy/0_128.jpg\", \"./images_sized/soft-candy/0_256.jpg\", \"./images_sized/soft-candy/0_512.jpg\", \"./images_sized/soft-candy/0_768.jpg\"]'),
(100, '[3]', 'Tootsie Pop Drops - 24ct', 'What do you get if you take a classic Tootsie Pop and remove the lollipop stick? You get original Tootsie Pop Drops! This unique confection offers the same delicious taste with a new design. Instead of a large lolly, you can get your Tootsie Pop fix with a bite-sized snack. Each piece is disc shaped with a hard candy outside and chewy candy center‚ just like the lollipops that inspired them! You\'ll find all your favorite Tootsie Roll flavors in this irresistible assortment. Try chocolate, orange, cherry, grape and blue raspberry or share them! Our bulk Tootsie Pop Drops gives you more pieces that are perfect for any purpose or occasion. Are you responsible for filling up the office candy jar? Save money by buying these delicious treats in bulk!Add them to party favors or use them as a quick snack to serve visitors who stop by. There\'s a lot of flavor to love when you have bulk Tootsie Pop Drops in your pantry!', 57.99, '[\"./images_sized/king-size-theater-boxes/100_64.jpg\", \"./images_sized/king-size-theater-boxes/100_96.jpg\", \"./images_sized/king-size-theater-boxes/100_128.jpg\", \"./images_sized/king-size-theater-boxes/100_256.jpg\", \"./images_sized/king-size-theater-boxes/100_512.jpg\", \"./images_sized/king-size-theater-boxes/100_768.jpg\"]'),
(200, '[5, 28]', 'Basketball Gumballs 4-Piece Tubes Vidal - 12ct', 'Vidal Basketball Gumballs 4-Piece 1.4oz - 12ct', 21.99, '[\"./images_sized/gum-bubblegum-candy/200_64.jpg\", \"./images_sized/gum-bubblegum-candy/200_96.jpg\", \"./images_sized/gum-bubblegum-candy/200_128.jpg\", \"./images_sized/gum-bubblegum-candy/200_256.jpg\", \"./images_sized/gum-bubblegum-candy/200_512.jpg\", \"./images_sized/gum-bubblegum-candy/200_768.jpg\", \"./images_sized/sports-candy/200_64.jpg\", \"./images_sized/sports-candy/200_96.jpg\", \"./images_sized/sports-candy/200_128.jpg\", \"./images_sized/sports-candy/200_256.jpg\", \"./images_sized/sports-candy/200_512.jpg\", \"./images_sized/sports-candy/200_768.jpg\"]'),
(300, '[8, 31]', 'Mini Gummi Worms Sugar Free - 5lb', 'Get your sweet fix and enjoy the fruity, juicy flavor of Albanese sugar free mini gummy worms! Gummy worms are a classic candy that has earned a large following. They were originally introduced to honor the 60th anniversary of the gummy bear. Even though they came later, many candy lovers prefer the long, wiggly shape that makes these long, wiggly worms so enticing. Albanese has created an irresistible gummy worm that\'s also better for your diet! Our sugar free mini gummy worms offer the fruit taste you love without the unnecessary sugar. Each package includes an assortment of popular flavors, including green apple, wild cherry, orange, lemon and pineapple. Satisfy your taste buds and stick to a low sugar diet. Sugar free gummies in bulk are a great choice for parties, events and classrooms. Educators can reward children without adding sugar to their daily diet while parents can offer an after school snack that\'s healthier. ', 69.99, '[\"./images_sized/mini-sized-candy/300_64.jpg\", \"./images_sized/mini-sized-candy/300_96.jpg\", \"./images_sized/mini-sized-candy/300_128.jpg\", \"./images_sized/mini-sized-candy/300_256.jpg\", \"./images_sized/mini-sized-candy/300_512.jpg\", \"./images_sized/mini-sized-candy/300_768.jpg\", \"./images_sized/sugar-free-candy/300_64.jpg\", \"./images_sized/sugar-free-candy/300_96.jpg\", \"./images_sized/sugar-free-candy/300_128.jpg\", \"./images_sized/sugar-free-candy/300_256.jpg\", \"./images_sized/sugar-free-candy/300_512.jpg\", \"./images_sized/sugar-free-candy/300_768.jpg\"]'),
(400, '[17, 24]', 'Micro Jawbreakers - Assorted - 10lb', 'Micro jawbreakers take the irresistible taste of big jawbreakers and packs it all into a compact treat. Children have savored the sweet flavors of this popular candy for years. Simply pop one in your mouth and let your taste buds experience an assortment of fruity flavors. Micro jawbreakers may not be as big, but these quarter-inch tidbits still pack powerful flavor! They are perfect for a quick treat that doesn\'t require hours of licking. Our bulk jawbreaker package includes a generous quantity of vibrantly colored pieces. Try your luck with red, green, yellow, orange or blue! The rainbow jawbreaker assortment is wonderful for birthday parties with colorful decor!You can also pour a handful into a treat bag to give as party favors or to pass out on Halloween. Our bulk candy package will give you plenty of miniature jawbreakers to go around √ê even if you\'re hosting an event with a large group!', 58.99, '[\"./images_sized/candy-coated-candy/400_64.jpg\", \"./images_sized/candy-coated-candy/400_96.jpg\", \"./images_sized/candy-coated-candy/400_128.jpg\", \"./images_sized/candy-coated-candy/400_256.jpg\", \"./images_sized/candy-coated-candy/400_512.jpg\", \"./images_sized/candy-coated-candy/400_768.jpg\", \"./images_sized/jawbreakers-candy/400_64.jpg\", \"./images_sized/jawbreakers-candy/400_96.jpg\", \"./images_sized/jawbreakers-candy/400_128.jpg\", \"./images_sized/jawbreakers-candy/400_256.jpg\", \"./images_sized/jawbreakers-candy/400_512.jpg\", \"./images_sized/jawbreakers-candy/400_768.jpg\"]'),
(500, '[26]', 'Extreme Cinnamon Juju Bears - 15lb Bulk', 'Red Hot Cinnamon Gummy Bears - 15lb', 69.99, '[\"./images_sized/hot-spicy-candy/500_64.jpg\", \"./images_sized/hot-spicy-candy/500_96.jpg\", \"./images_sized/hot-spicy-candy/500_128.jpg\", \"./images_sized/hot-spicy-candy/500_256.jpg\", \"./images_sized/hot-spicy-candy/500_512.jpg\", \"./images_sized/hot-spicy-candy/500_768.jpg\"]'),
(600, '[34]', 'Mounds Bars - 36ct', 'Palm trees. Turquoise ocean water. Cool drinks in your hand. Take your mouth on an indulgent island escape with these classic Mounds bars! The fluffy coconut and creamy dark chocolate of world-famous, Mounds, will make you feel far, far away on a tropical getaway. A sibling to the also famous, Almond Joy, they were rocketed into stardom in the 197s with the slogan, \'\'Sometimes you feel like a nut, sometimes you don\'t . \'\' We just know that you\'ll feel relaxed and pampered with every coconutty bite. Stock up on these for a savory treat any time of the year, to add to lucky trick-or-treaters\' bags, or to give away in a gourmet chocolate basket. ', 75.99, '[\"./images_sized/retro/600_64.jpg\", \"./images_sized/retro/600_96.jpg\", \"./images_sized/retro/600_128.jpg\", \"./images_sized/retro/600_256.jpg\", \"./images_sized/retro/600_512.jpg\", \"./images_sized/retro/600_768.jpg\"]');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `category_id` int NOT NULL COMMENT 'Unique identifier',
  `name` varchar(64) NOT NULL COMMENT 'Name of Category',
  `candy_ids` json NOT NULL COMMENT 'Json list of candy Id''s in this category'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int NOT NULL COMMENT 'unique identifier',
  `first_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'first name of user',
  `last_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'last name of user',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'optional username',
  `email` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'users email (no really its an email address)(',
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'hashed password'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `username`, `email`, `password`) VALUES
(51, 'terry', 'griffin', 'rugbyprof', 'proff.griff@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'),
(52, 'bob', 'smith', 'bobbyboy', 'bob@bob.com', '81b637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9'),
(53, 'lucy', 'lovelace', 'lucygirl', 'lucy@bob.com', 'dc99e9aa86fab83a062cff5e0808391757071a3d5dbb942802d5f923aaead3b4'),
(54, 'angel', 'badillo', '', 'angel@badill.com', '1bc97520d648ac73a954f8c56610d81f07511070c402b7fa0353b698597212d1'),
(55, 'freddy', 'mack', 'fmack', 'freddy@mack.com', '1eb8aef1779d74fc1cc070035946a4a519d20bd0d8c5c773ca3f6208bc96eeaa'),
(56, 'Rachel', 'Griffin', 'Rdog', 'Rdog@therdogpound.com', '972964b66bdfe6b5b181c5112a6a0470204f64661ee7e3efb9aab0ce3cc403ff');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candy`
--
ALTER TABLE `candy`
  ADD PRIMARY KEY (`candy_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT COMMENT 'unique identifier', AUTO_INCREMENT=57;
COMMIT;
