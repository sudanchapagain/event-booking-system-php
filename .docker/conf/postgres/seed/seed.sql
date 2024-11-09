INSERT INTO users (username, user_phone, email, password_hash, is_organizer, is_admin)
VALUES 
    ('JohnDoe', '1234567890', 'john.d@example.com', '$2y$10$5e0A5sXZX9ZV9/sNQfPxm2F4Fdpj6Af5b4U8n5j7Ic2cNoB2Vf93q', FALSE, FALSE),
    ('JaneSmith', '0987654321', 'jane.s@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n2', TRUE, TRUE),
    ('MaryJohnson', '1122334455', 'mary.j@example.com', '$2y$10$5e0A5sXZX9ZV9/sNQfPxm2F4Fdpj6Af5b4U8n5j7Ic2cNoB2Vf93q', FALSE, TRUE),
    ('AliceBrown', '2233445566', 'alice.b@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n3', FALSE, FALSE),
    ('BobGreen', '3344556677', 'bob.g@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n4', FALSE, FALSE),
    ('CharlieWhite', '4455667788', 'charlie.w@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n5', TRUE, FALSE),
    ('DavidBlack', '5566778899', 'david.b@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5mIj2jPwvNjy6dNPeZrOL8n6', FALSE, FALSE, FALSE),
    ('EvaBlue', '6677889900', 'eva.b@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n7', FALSE, TRUE),
    ('FrankGrey', '7788990011', 'frank.g@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n8', FALSE, FALSE),
    ('GracePink', '8899001122', 'grace.p@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n9', FALSE, FALSE),
    ('HarryYellow', '9900112233', 'harry.y@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n10', TRUE, TRUE),
    ('IvyPurple', '1011122233', 'ivy.p@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n11', FALSE, FALSE),
    ('JackRed', '1122334455', 'jack.r@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n12', TRUE, FALSE),
    ('KimWhite', '2233445566', 'kim.w@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n13', FALSE, FALSE),
    ('LiamOrange', '3344556677', 'liam.o@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n14', FALSE, FALSE),
    ('MiaCyan', '4455667788', 'mia.c@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n15', FALSE, FALSE),
    ('NoahViolet', '5566778899', 'noah.v@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n16', TRUE, FALSE),
    ('OliviaBrown', '6677889900', 'olivia.b@example.com', '$2y$10$Jl4YXQyG/XsY8wh7Y9AmCh5F7AzJ5cmIj2jPwvNjy6dNPeZrOL8n17', FALSE, TRUE);

INSERT INTO events (title, location, description, organizer_id, capacity, notice, terms_and_conditions, refund_policy)
VALUES 
    ('Tech Conference 2024', 'New York, USA', 'A conference about the latest in tech.', 1, 500, 'No refunds after 30 days.', 'Terms and conditions of Tech Conference.', 'Refund available within 30 days.'),
    ('Music Festival 2024', 'Los Angeles, USA', 'A music festival featuring top bands and artists.', 2, 1000, 'Early bird tickets available.', 'Terms and conditions for the music festival.', 'Refund available within 60 days.'),
    ('Business Summit 2024', 'Chicago, USA', 'A summit for business leaders and entrepreneurs.', 3, 300, 'Discounts available for early registrants.', 'Business summit terms and conditions.', 'No refund after 15 days.'),
    ('Art Expo 2024', 'Paris, France', 'An exhibition of contemporary art.', 4, 150, 'Opening reception available.', 'Terms of Art Expo.', 'Refund available within 45 days.'),
    ('EduCon 2024', 'London, UK', 'A conference for educators and students.', 5, 200, 'Early bird tickets available until June.', 'EduCon 2024 terms and conditions.', 'Refund within 30 days of registration.'),
    ('Gaming Expo 2024', 'San Francisco, USA', 'The biggest gaming expo of the year.', 6, 1000, 'Exclusive offers for VIP tickets.', 'Gaming Expo terms and conditions.', 'Refund available before the event date.'),
    ('TechTalk 2024', 'Austin, USA', 'A tech talk featuring industry leaders.', 7, 500, 'Seats limited for VIP attendees.', 'TechTalk event policies.', 'No refunds after the event starts.'),
    ('Music Live 2024', 'Miami, USA', 'Live performances from top musicians.', 8, 800, 'Tickets include free merchandise.', 'Music Live event policies.', 'Refunds only available before ticket sale ends.'),
    ('Film Fest 2024', 'Berlin, Germany', 'A festival showcasing new films and directors.', 9, 400, 'Tickets available for student discounts.', 'Film Fest terms and conditions.', 'Refund available before event date.'),
    ('FoodFest 2024', 'Tokyo, Japan', 'A food festival celebrating world cuisine.', 10, 600, 'Free snacks for the first 1000 attendees.', 'FoodFest event policies.', 'Refunds available up to 3 days before event.'),
    ('Sports Expo 2024', 'Los Angeles, USA', 'An exhibition for sports fans and professionals.', 11, 500, 'VIP tickets get special access.', 'Sports Expo terms and conditions.', 'Refund available within 30 days of registration.'),
    ('Wellness 2024', 'Seattle, USA', 'A wellness event promoting healthy living.', 12, 400, 'Discounts for early registrants.', 'Wellness event terms and conditions.', 'Refund available up to a week before event.'),
    ('Startup Expo 2024', 'San Francisco, USA', 'A networking event for startups and investors.', 13, 300, 'Networking opportunities for all attendees.', 'Startup Expo terms and conditions.', 'Refunds not available after registration deadline.'),
    ('Fashion Week 2024', 'New York, USA', 'A fashion week event showcasing new designers.', 14, 1000, 'Early bird tickets get VIP seating.', 'Fashion Week terms and conditions.', 'Refunds available within 14 days.'),
    ('Health Summit 2024', 'London, UK', 'A summit for healthcare professionals.', 15, 400, 'Discounts available for group tickets.', 'Health Summit terms and conditions.', 'Refund available before the event date.'),
    ('DevCon 2024', 'San Francisco, USA', 'A developer conference for software professionals.', 16, 700, 'Early access tickets with exclusive perks.', 'DevCon terms and conditions.', 'Refunds allowed before event date.'),
    ('EduExhibit 2024', 'Berlin, Germany', 'An exhibition of educational resources and tools.', 17, 300, 'Special discounts for students and teachers.', 'EduExhibit terms and conditions.', 'Refund available within 30 days.'),
    ('Marketing Expo 2024', 'Los Angeles, USA', 'A marketing conference featuring industry experts.', 18, 500, 'Discounts for early bird tickets.', 'Marketing Expo terms and conditions.', 'Refund available up to 14 days before event.'),
    ('Photographers Meet 2024', 'Tokyo, Japan', 'A gathering of professional photographers.', 19, 200, 'Free merchandise for VIP ticket holders.', 'Photographers Meet terms and conditions.', 'Refunds available before event date.'),
    ('VR Expo 2024', 'London, UK', 'An expo showcasing the latest in virtual reality technology.', 20, 1000, 'VIP tickets provide exclusive VR demos.', 'VR Expo terms and conditions.', 'Refund available within 30 days.');

INSERT INTO event_categories (name) 
VALUES 
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

INSERT INTO event_category_mapping (event_id, category_id) 
VALUES 
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
    (19, 3),
    (20, 1);

INSERT INTO tickets (event_id, ticket_type, ticket_price)
VALUES 
    (1, 'General Admission', 100.00),
    (1, 'VIP', 250.00),
    (2, 'General Admission', 50.00),
    (2, 'VIP', 150.00),
    (3, 'General Admission', 80.00),
    (3, 'VIP', 180.00),
    (4, 'Standard', 40.00),
    (4, 'VIP', 120.00),
    (5, 'Student', 60.00),
    (5, 'Professional', 120.00),
    (6, 'Early Bird', 75.00),
    (6, 'General Admission', 125.00),
    (7, 'Standard', 50.00),
    (7, 'VIP', 150.00),
    (8, 'General Admission', 90.00),
    (8, 'VIP', 250.00),
    (9, 'Student', 60.00),
    (9, 'General Admission', 120.00),
    (10, 'General Admission', 70.00),
    (10, 'VIP', 200.00),
    (11, 'VIP', 250.00),
    (11, 'Standard', 100.00),
    (12, 'General Admission', 50.00),
    (12, 'VIP', 175.00),
    (13, 'Student', 60.00),
    (13, 'Professional', 150.00),
    (14, 'General Admission', 120.00),
    (14, 'VIP', 200.00),
    (15, 'Standard', 70.00),
    (15, 'VIP', 175.00),
    (16, 'Early Bird', 90.00),
    (16, 'VIP', 160.00),
    (17, 'Standard', 50.00),
    (17, 'VIP', 120.00),
    (18, 'General Admission', 90.00),
    (18, 'VIP', 180.00),
    (19, 'General Admission', 60.00),
    (19, 'VIP', 140.00),
    (20, 'General Admission', 50.00),
    (20, 'VIP', 130.00);

INSERT INTO faqs (event_id, question, answer)
VALUES 
    (1, 'What is the dress code?', 'Business casual is recommended.'),
    (1, 'Will food be provided?', 'Yes, lunch and dinner will be provided.'),
    (1, 'Is parking available?', 'Yes, parking is available on-site.'),
    (1, 'Are there networking opportunities?', 'Yes, networking sessions will be held throughout the event.'),
    (1, 'Can I get a refund if I cannot attend?', 'Refunds are available within 30 days of purchase.'),
    (1, 'Will there be any guest speakers?', 'Yes, prominent industry leaders will speak at the event.'),
    
    (2, 'What is the age limit?', 'All ages are welcome!'),
    (2, 'Are pets allowed?', 'Sorry, no pets allowed.'),
    (2, 'Can I re-enter the event if I leave?', 'Yes, re-entry is allowed with a wristband.'),
    (2, 'Is there a dress code?', 'Casual attire is recommended.'),
    (2, 'Will there be merchandise for sale?', 'Yes, event merchandise will be available for purchase.'),
    (2, 'Are there accommodations for people with disabilities?', 'Yes, the venue is accessible and has accommodations.'),
    
    (3, 'What is the refund policy?', 'Refunds available within 15 days.'),
    (3, 'Is there a dress code?', 'Business casual attire is recommended.'),
    (3, 'Are meals provided?', 'Lunch and coffee breaks are included.'),
    (3, 'Is Wi-Fi available?', 'Yes, free Wi-Fi will be available to all attendees.'),
    (3, 'Can I bring a guest?', 'Guests are allowed with a purchased guest ticket.'),
    (3, 'Is there an early-bird ticket discount?', 'Yes, early-bird discounts are available.'),
    
    (4, 'What time does the event start?', 'The event starts at 9:00 AM.'),
    (4, 'Can I bring my pet?', 'Sorry, pets are not allowed at this event.'),
    (4, 'Are children allowed?', 'This event is open to adults only.'),
    (4, 'Will there be a Q&A session?', 'Yes, each session includes a Q&A segment.'),
    (4, 'Is there a VIP package available?', 'Yes, the VIP package includes front-row seating and a meet-and-greet.'),
    (4, 'Will there be photography at the event?', 'Yes, a photographer will capture key moments.'),
    
    (5, 'Do you provide parking?', 'Yes, there is ample parking available.'),
    (5, 'Is lunch provided?', 'Lunch will be served at the event.'),
    (5, 'Are there special rates for students?', 'Yes, students receive a discount with a valid ID.'),
    (5, 'What time does the event end?', 'The event ends at 5:00 PM.'),
    (5, 'Is there a post-event networking session?', 'Yes, networking sessions are available after the main event.'),
    (5, 'Are breakout sessions included?', 'Yes, attendees can participate in breakout sessions.'),
    
    (6, 'Can I buy tickets at the door?', 'Tickets are available online only.'),
    (6, 'What is the location?', 'The event will take place at the convention center.'),
    (6, 'Will there be a live-stream option?', 'Yes, online access is available for virtual attendees.'),
    (6, 'Can I volunteer for the event?', 'Yes, volunteer applications are open on the event website.'),
    (6, 'What items are prohibited?', 'Outside food, beverages, and large bags are not allowed.'),
    (6, 'Is there a lost and found?', 'Yes, lost items can be claimed at the help desk.'),
    
    (7, 'Are there group discounts?', 'Yes, group discounts are available for 10 or more people.'),
    (7, 'Can I transfer my ticket?', 'Tickets are non-transferable.'),
    (7, 'Are there any workshops?', 'Yes, multiple workshops will be held throughout the day.'),
    (7, 'Is the venue wheelchair accessible?', 'Yes, the venue is fully accessible.'),
    (7, 'Will there be on-site registration?', 'On-site registration is not available; please register in advance.'),
    (7, 'Are sessions recorded for later viewing?', 'Yes, recorded sessions are available to attendees.'),
    
    (8, 'What time does the event end?', 'The event ends at midnight.'),
    (8, 'Will there be VIP seating?', 'Yes, VIP seating will be available at the front.'),
    (8, 'Are outside food and drinks allowed?', 'No, outside food and drinks are not permitted.'),
    (8, 'Is there a shuttle service to the venue?', 'Yes, complimentary shuttles are available from key locations.'),
    (8, 'What is the smoking policy?', 'This is a smoke-free event.'),
    (8, 'Will there be a cloakroom?', 'Yes, cloakroom services are available for attendees.'),
    
    (9, 'How many people can attend?', 'The event can accommodate up to 400 people.'),
    (9, 'Are drinks included?', 'Drinks will be available for purchase.'),
    (9, 'Can I bring a camera?', 'Personal photography is allowed, but no flash.'),
    (9, 'Is there a dress code?', 'Smart casual is recommended.'),
    (9, 'What time do doors open?', 'Doors open at 8:00 AM.'),
    (9, 'Are there reserved seats?', 'Seats are available on a first-come, first-served basis.'),
    
    (10, 'Is there a coat check?', 'Yes, there will be a coat check available.'),
    (10, 'Are there any discounts?', 'Discounts are available for early registrants.'),
    (10, 'Is this a family-friendly event?', 'Yes, children are welcome with adult supervision.'),
    (10, 'Can I get a refund?', 'Refunds are available within 14 days of ticket purchase.'),
    (10, 'Are there vegetarian options available?', 'Yes, vegetarian options are provided.'),
    (10, 'Is there a mobile app for the event?', 'Yes, download the event app for schedules and updates.');

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
    (6, 13),
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

INSERT INTO promocodes (event_id, promocode, discount_percentage)
VALUES 
    (1, 'TECH2024', 10.00),
    (2, 'MUSIC2024', 15.00),
    (3, 'BUSINESS2024', 5.00),
    (4, 'ART2024', 20.00),
    (5, 'EDU2024', 10.00),
    (6, 'GAMING2024', 25.00),
    (7, 'TECHTALK2024', 15.00),
    (8, 'MUSICLIVE2024', 10.00),
    (9, 'FILMFEST2024', 10.00),
    (10, 'FOODFEST2024', 5.00),
    (11, 'SPORTSEXPO2024', 20.00),
    (12, 'WELLNESS2024', 15.00),
    (13, 'STARTUPEXPO2024', 10.00),
    (14, 'FASHIONWEEK2024', 5.00),
    (15, 'HEALTHSUMMIT2024', 20.00),
    (16, 'DEVCON2024', 25.00),
    (17, 'EDUEXHIBIT2024', 10.00),
    (18, 'MARKETINGEXPO2024', 20.00),
    (19, 'PHOTOMEDIA2024', 15.00),
    (20, 'VREXPO2024', 30.00);

INSERT INTO event_images (event_id, image_url, image_type)
VALUES 
    (1, 'seed_data/images/tech-conference.jpg', 'image/jpeg'),
    (2, 'seed_data/images/music-festival.jpg', 'image/jpeg'),
    (3, 'seed_data/images/business-conference.jpg', 'image/jpeg'),
    (4, 'seed_data/images/arts-festival.jpg', 'image/jpeg'),
    (5, 'seed_data/images/edu-conference.jpg', 'image/jpeg'),
    (6, 'seed_data/images/gaming-expo.jpg', 'image/jpeg'),
    (7, 'seed_data/images/tech-talk.jpg', 'image/jpeg'),
    (8, 'seed_data/images/music-live.jpg', 'image/jpeg'),
    (9, 'seed_data/images/film-festival.jpg', 'image/jpeg'),
    (10, 'seed_data/images/food-festival.jpg', 'image/jpeg'),
    (11, 'seed_data/images/sports-expo.jpg', 'image/jpeg'),
    (12, 'seed_data/images/wellness-summit.jpg', 'image/jpeg'),
    (13, 'seed_data/images/startup-expo.jpg', 'image/jpeg'),
    (14, 'seed_data/images/fashion-week.jpg', 'image/jpeg'),
    (15, 'seed_data/images/health-summit.jpg', 'image/jpeg'),
    (16, 'seed_data/images/devcon.jpg', 'image/jpeg'),
    (17, 'seed_data/images/eduexhibit.jpg', 'image/jpeg'),
    (18, 'seed_data/images/marketing-expo.jpg', 'image/jpeg'),
    (19, 'seed_data/images/photographers-meet.jpg', 'image/jpeg'),
    (20, 'seed_data/images/vr-expo.jpg', 'image/jpeg');

INSERT INTO event_dates (event_id, start_date, end_date)
VALUES 
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
