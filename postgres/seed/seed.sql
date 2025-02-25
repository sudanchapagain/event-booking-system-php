INSERT INTO users (username, user_phone, email, password_hash, is_organizer, is_admin) VALUES 
    ('RamThapa', '9801234567', 'ram.t@example.com', '$2y$10$5e0A5sXZX9ZV9/sNQfPxm2F4Fdpj6Af5b4U8n5j7Ic2cNoB2Vf93q', FALSE, FALSE),
    ('SitaShrestha', '9802345678', 'sita.s@example.com', '$2y$10$Jl4YXQyG/XsY8Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n2', TRUE, TRUE),
    ('GitaGurung', '9803456789', 'gita.g@example.com', '$2y$10$5e0A5sXZX9ZV9/sNQfPxm4Fdpj6Af5b4U8n5j7Ic2cNoB2Vf93q', FALSE, TRUE),
    ('BikashLama', '9804567890', 'bikash.l@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9A7AzJdcmIj2jPwvNjy6dNPeZrOL8n3', FALSE, FALSE),
    ('KumarRai', '9805678901', 'kumar.r@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7zJcmIj2jPwvNjy6dNPeZrOL8n4', FALSE, FALSE),
    ('SaritaMagar', '9806789012', 'sarita.m@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmChJ5cmIj2jPwvNjy6dNPeZrOL8n5', TRUE, FALSE),
    ('RajendraKarki', '9807890123', 'rajendra.k@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9A5mIj2jPwvNjy6dNPeZrOL8n6', FALSE, FALSE),
    ('MayaTamang', '9808901234', 'maya.t@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7A5cmIj2jPwvNjy6dNPeZrOL8n7', FALSE, TRUE),
    ('SantoshKC', '9810012345', 'santosh.kc@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5cmIj2jPwvNjy6dNPeZrOL8n8', FALSE, FALSE),
    ('AnjaliSharma', '9811123456', 'anjali.s@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmChcmIj2jPwvNjy6dNPeZrOL8n9', FALSE, FALSE),
    ('KeshavPoudel', '9812234567', 'keshav.p@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5cmIj2jPwvNjy6dNPeZrOL8n10', TRUE, TRUE),
    ('SunitaDhakal', '9813345678', 'sunita.d@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F72jPwvNjy6dNPeZrOL8n11', FALSE, FALSE),
    ('ManishAdhikari', '9814456789', 'manish.a@example.com', '$2y$10$Jl4YXG/XsY8wh7Y9AmCh5F7A2jPwvNjy6dNPeZrOL8n12', TRUE, FALSE),
    ('PujaRana', '9815567890', 'puja.r@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIjPwvNjy6dNPeZrOL8n13', FALSE, FALSE),
    ('RajanSharma', '9816678901', 'rajan.s@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cwvNjy6dNPeZrOL8n14', FALSE, FALSE),
    ('MeenaBhattarai', '9817789012', 'meena.b@example.com', '$2y$10$Jl4YXQyG/XsY8w9AmCh5F7AzJ5cwvNjy6dNPeZrOL8n15', FALSE, FALSE),
    ('SanjayKharel', '9818890123', 'sanjay.k@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJPwvNjy6dNPeZrOL8n16', TRUE, FALSE),
    ('PratimaBasnet', '9819901234', 'pratima.b@example.com', '$2y$10$Jl4YXQyG/XsY87Y9AmCh5F7AzJ5cvNjy6dNPeZrOL8n17', FALSE, TRUE);

INSERT INTO events (title, location, description, organizer_id, capacity, ticket_price, is_approved) VALUES 
    ('Tech Meetup Kathmandu', 'Kathmandu, Nepal', 'A gathering of tech enthusiasts and developers.', 1, 150, 100, false),
    ('Indie Music Night', 'Lalitpur, Nepal', 'An evening of indie music performances by local artists.', 2, 200, 0, false),
    ('Startup Founders Forum', 'Bhaktapur, Nepal', 'A meetup for aspiring entrepreneurs and startup founders.', 3, 50, 200, false),
    ('Art House Exhibition', 'Kathmandu, Nepal', 'An exhibition showcasing local contemporary art.', 4, 100, 50, false),
    ('Teachers and Learners Summit', 'Lalitpur, Nepal', 'A conference for educators and students.', 5, 150, 0, false),
    ('Gaming Meetup Nepal', 'Kathmandu, Nepal', 'A meetup for gamers to showcase and play new games.', 6, 300, 150, false),
    ('TechTalk Nepal', 'Bhaktapur, Nepal', 'A tech talk featuring local tech pioneers.', 7, 200, 100, false),
    ('Live Music Jam', 'Pokhara, Nepal', 'Live performances by emerging local musicians.', 8, 300, 0, false),
    ('Short Film Screening', 'Kathmandu, Nepal', 'A screening of short films by local filmmakers.', 9, 100, 50, false),
    ('Food and Culture Fair', 'Patan, Nepal', 'A celebration of Nepali food and cultural heritage.', 10, 400, 0, false),
    ('Sports Enthusiasts Meetup', 'Lalitpur, Nepal', 'A meetup for sports fans to discuss and play.', 11, 150, 100, false),
    ('Health and Wellness Day', 'Kathmandu, Nepal', 'An event promoting healthy living and wellness practices.', 12, 250, 0, false),
    ('Local Startup Exhibition', 'Bhaktapur, Nepal', 'An exhibition for local startups to showcase their ideas.', 13, 100, 50, false),
    ('Fashion Fiesta Kathmandu', 'Kathmandu, Nepal', 'A fashion event featuring young designers.', 14, 300, 150, false),
    ('Healthcare Innovation Summit', 'Lalitpur, Nepal', 'A summit focusing on innovations in healthcare.', 15, 150, 0, false),
    ('Developers Meetup Nepal 2024', 'Kathmandu, Nepal', 'A conference for software developers in Nepal.', 16, 250, 200, false),
    ('Educational Resource Exhibit', 'Patan, Nepal', 'An exhibition of educational tools and resources.', 17, 200, 0, false),
    ('Marketing Workshop Kathmandu', 'Kathmandu, Nepal', 'A workshop on modern marketing techniques.', 18, 150, 100, false),
    ('Photographers Showcase', 'Pokhara, Nepal', 'An event featuring the work of local photographers.', 19, 100, 50, false);

INSERT INTO event_categories (name) VALUES 
    ('Technology'),
    ('Music'),
    ('Arts'),
    ('Business'),
    ('Education'),
    ('Gaming'),
    ('Sports'),
    ('Health'),
    ('Wellness'),
    ('Fashion'),
    ('Food'),
    ('Film'),
    ('Marketing'),
    ('Networking'),
    ('Startup'),
    ('Developer'),
    ('Education Resources'),
    ('Tech Innovation'),
    ('Entertainment'),
    ('Lifestyle');

INSERT INTO event_category_mapping (event_id, category_id) VALUES 
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 3),
    (5, 5),
    (6, 6),
    (7, 1),
    (8, 2),
    (9, 3),
    (10, 7),
    (11, 8),
    (12, 9),
    (13, 10),
    (14, 11),
    (15, 8),
    (16, 1),
    (17, 5),
    (18, 4),
    (19, 3);

INSERT INTO user_event_attendance (user_id, event_id)
VALUES 
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (4, 8),
    (4, 9),
    (5, 10),
    (5, 11),
    (6, 12),
    (6, 13),
    (7, 14),
    (7, 15),
    (8, 16),
    (8, 17),
    (9, 18),
    (9, 19),
    (10, 20),
    (10, 1),
    (11, 2),
    (11, 3),
    (12, 4),
    (12, 5),
    (13, 6),
    (13, 7),
    (14, 8),
    (14, 9),
    (15, 10),
    (15, 11),
    (16, 12),
    (16, 13),
    (17, 14),
    (17, 15),
    (18, 16),
    (18, 17),
    (19, 18),
    (19, 19),
    (20, 20),
    (1, 18),
    (2, 17),
    (3, 16),
    (4, 15),
    (5, 14),
    (7, 12),
    (8, 11),
    (9, 10),
    (10, 9),
    (11, 8),
    (12, 7),
    (13, 6),
    (14, 5),
    (15, 4),
    (16, 3),
    (17, 2),
    (18, 1),
    (19, 20),
    (20, 19);

INSERT INTO event_images (event_id, image_url, image_type)
VALUES 
    (1, 'seed_data/images/1.jpg', 'image/jpeg'),
    (2, 'seed_data/images/2.jpg', 'image/jpeg'),
    (3, 'seed_data/images/3.jpg', 'image/jpeg'),
    (4, 'seed_data/images/4.jpg', 'image/jpeg'),
    (5, 'seed_data/images/5.jpg', 'image/jpeg'),
    (6, 'seed_data/images/6.jpg', 'image/jpeg'),
    (7, 'seed_data/images/7.jpg', 'image/jpeg'),
    (8, 'seed_data/images/8.jpg', 'image/jpeg'),
    (9, 'seed_data/images/9.jpg', 'image/jpeg'),
    (10, 'seed_data/images/10.jpg', 'image/jpeg'),
    (11, 'seed_data/images/11.jpg', 'image/jpeg'),
    (12, 'seed_data/images/12.jpg', 'image/jpeg'),
    (13, 'seed_data/images/13.jpg', 'image/jpeg'),
    (14, 'seed_data/images/14.jpg', 'image/jpeg'),
    (15, 'seed_data/images/15.jpg', 'image/jpeg'),
    (16, 'seed_data/images/16.jpg', 'image/jpeg'),
    (17, 'seed_data/images/17.jpg', 'image/jpeg'),
    (18, 'seed_data/images/18.jpg', 'image/jpeg'),
    (19, 'seed_data/images/19.jpg', 'image/jpeg');

INSERT INTO event_dates (event_id, start_date, end_date) VALUES 
    (1, '2024-10-01 09:00:00', '2024-10-01 17:00:00'),
    (2, '2024-11-15 12:00:00', '2024-11-15 23:59:59'),
    (3, '2024-12-05 09:00:00', '2024-12-05 18:00:00'),
    (4, '2024-12-10 10:00:00', '2024-12-10 20:00:00'),
    (5, '2025-01-10 08:00:00', '2025-01-10 17:00:00'),
    (6, '2025-02-14 09:00:00', '2025-02-14 18:00:00'),
    (7, '2025-03-01 08:00:00', '2025-03-01 18:00:00'),
    (8, '2025-04-02 11:00:00', '2025-04-02 23:59:59'),
    (9, '2025-05-06 09:00:00', '2025-05-06 17:00:00'),
    (10, '2025-06-12 12:00:00', '2025-06-12 23:59:59'),
    (11, '2025-07-15 09:00:00', '2025-07-15 17:00:00'),
    (12, '2025-08-20 08:00:00', '2025-08-20 18:00:00'),
    (13, '2025-09-02 10:00:00', '2025-09-02 20:00:00'),
    (14, '2025-10-10 09:00:00', '2025-10-10 18:00:00'),
    (15, '2025-11-06 10:00:00', '2025-11-06 17:00:00'),
    (16, '2025-12-04 09:00:00', '2025-12-04 17:00:00'),
    (17, '2025-12-15 09:00:00', '2025-12-15 17:00:00'),
    (18, '2025-12-20 09:00:00', '2025-12-20 17:00:00'),
    (19, '2025-12-30 09:00:00', '2025-12-30 17:00:00'),
    (20, '2025-12-31 09:00:00', '2025-12-31 17:00:00');
