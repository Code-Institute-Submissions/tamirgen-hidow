# Hidow
------------------

Hidow is a B2C website that was designed to accommodate and to be an eCommerce platform for users who are 
interested in buying TENS and EMS devices.
Hidow provides the best-in-class devices and accessories for the devices that can be placed on almost every part of the body for pain relief, muscle stimulation, and recovery from training and injuries.
The website is very intuitive and provides a seamless customer journey from the page landing to checkout.
In addition, the website allows to read and write reviews about selected products that the website admin enables or disables from the app itself or the admin panel.


[Here is a link to the live version of the App](https://hidow.herokuapp.com/)

![Responsive Mockup](https://github.com/tamirgen/hidow/blob/main/media/mocup-Hidow.jpg?raw=true)

<br>

## User Experience (UX)
----------------------

### Project Goals
-----------------
* The website should have an intuitive and minimalist design, appealing to the customers.
* Allow users to be able to sort the products with a lot of sorting options and to make an informed decision based on previous customers' reviews.
* Provide the users with a post-purchase summary, confirmation email, and an option to store their data for future orders and to view past orders.
* Make sure the users' data is safe by offering secure login and by using Stripe as a secure online transactions expertise.


### User Stories
----------------
* As a website user I can see a list of products so that I can choose the product I would like to buy
* As a website user I can select a category so that I can easily find products
* As a website user I can get details so that I can see the price, product description, and sizes, when there are ones
* As a website user I can see the shopping bag so that I can know how much I have spent so far
* As a website user I can register for an account so that I can see my order history and store my personal details
* As a website user I can easily log in and out of the account so that I can save my address and personal data
* As a website user I can recover my password so that I can log in if I forgot my password
* As a website user I can get a confirmation email after registration so that I can know that the registration was successful
* As a website user I can sort the products so that I can easily identify the products based on price or category
* As a website user I can sort the products within a specific category so that I can compare products based on price and description
* As a website user I can sort the products by inserting the product name of title so that I can easily find the specific product I am looking for
* As a website user I can easily select the size and amount of products so that I can ensure I have the correct amounts and the right product amount
* As a website user I can see the items and the prices detailed in the shopping bag so that I can know what I am ordering and what will it cost me
* As a website user I can adjust my shopping bag so that I can make changes to my order before the checkout
* As a website user I can quickly enter my payment information so that I can checkout with no hassle
* As a website user I can get an order confirmation after the checkout so that I can verify I did not make any mistakes
* As a website user I can securely enter my payment information so that I can be sure my information will not be used by malicious users
* As a website user I can get an email after completing the checkout so that I can have all the information and a reminder of what I have purchased
* As a Site owner I can add a product so that I can add new items to my store
* As a Site owner I can edit existing products so that I can change prices, sizes, and descriptions if I need to
* As a Site owner I can delete an item so that remove items that are no longer for sale
* As a website user I can add a review so that other users can get an honest opinion on the products
* As a website user I can read reviews about products so that I can make a decision if to buy it
* As a website owner I can delete reviews so that I can leave just the ones I am using in the website
* As a website owner I can enable and disable the products reviews so that decide which products to allow getting reviewed

### Color Scheme
----------------
The colors used in the site are three different ones:
* The background is White: #ffffff
* The Text is black.
* The buttons and links are blue, light blue for positive actions, like updating orders and rating a product. They are white and black for standard actions like got to reviews or adding to bag and are red for removing a product from bag.
I have chosen those basic colors as for me they represent luxury and high-end products like the brand I have chosen to create the App for.
Those colors were also chosen to give the user good contrast between the background and text.


### Typography
--------------
The main font used in the site Sans-Serif. 

<br>

## Existing Features
--------------------
<br>

### General
-----------

* Responsive design across all device sizes.

* Similar color scheme and design throughout all pages to effectively structure, categorize and present the information to the customers.

* **Header**
-----------
![Header image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-header.jpg?raw=ture)
    
- The header contains the business name and a fully responsive navigation bar positioned across the top of the screen.

- The business name functions as a link to the landing page.

- The navigation bar is identical on all pages and contains links to all pages to facilitate navigation across the site.

* **The Navigation Bar**
------------------------

- The bar appears across all the website pages, and contains the following:
    - The product name, also serve as a home button.
    - The brands' categories.
    - A review tab that redirects users to leave a review.
    - Search bar, to easily find things on the website using search terms.
    - It contains the user's login and registration links. If the user is logged in, it contains the user's profile as well.
    - Shopping bag that stores the products that the user picked and presents the total amount of products picked so far.


   <br>

* **Footer**
------------
![Footer image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-footer.jpg?raw=true)

- The footer includes links to Facebook and Mailchimp newsletter.

- The footer contains a link to GDPR regulations file.

- All footer links will open in a new tab.

<br>

* **Landing Page**
----------------
![room categories](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/select-a-room.jpg?raw=true)

- The landing page contains the website header, 2 sections, and a footer.
- The main section is a cover image with an H2 headline and a call-to-action button for "Shop Now".
- The secondary section contains general information about the brand, the main benefits of using the products, and links to external links with further information.

<br>

* **Products page**
----------------------------
This page contains all the products and can be reached from the "Shop Now" button or the "ALL PRODUCTS" button in the main nav.

- The page has the following sorting options:
 - Sort by price, rating, or category.
 - Find specific products by using the search bar.
 - Additional sorting bar the sort by:
  * Price- low to high and vice versa.
  * Rating- low to high and vice versa.
  * Name- low to high and vice versa.
  * Category- low to high and vice versa.

- Every product has the following information:
  * Title
  * Category
  * Price
  * Rating
  * Image of the item

 ![room details and date selection](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-details-dates.jpg?raw=true)

<br>

* **Product Details page**
-----------------
- The page contains a detailed description of the product.
- Every product has the following information:
  * Title
  * Category
  * Price
  * Rating
  * Image of the item
- Under the description, there is a quantity selector, in case the user wants to get more than 1 item.
The selector can be used by writing the quantity, using the +\- buttons or the up|down arrows.
- Underneath the quantity selector there are 3 buttons:
    * ADD TO BAG- keeps the user on the same page, but updates the bag in the right top corner with the amount that was added to the bag so far.
    * KEEP SHOPPING- Sends the user back to the "ALL PRODUCTS" page. 
    * REVIEWS- Send the user to read the reviews about the product.

<br>

![room details in case not logged or registered](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-bookings-cancel-update.jpg?raw=true)

* **The Shopping Bag**
--------------------

- Clicking on the shopping bag icon will redirect the user to the shopping bag page (one step before the checkout).
- The user will have a summary of the products he collected, including: 
 * Product name.
 * Product image.
 * Size (if applicable).
 * Identifier.
 * Price.
 * Quantity.
 * Subtotal.

 ![room details in case not logged or registered](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-bookings-cancel-update.jpg?raw=true)

- In addition, the user can update his selection by using the same quantity selector as on the Product Details page, and additionally, he can remove the item completely from the bag.

- The bottom part of the page includes the total amount, delivery cost, the grand total, and 2 buttons.
One bottom to get to the checkout ("SECURE CHECKOUT") and the other to "KEEP SHOPPING".


![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-cancaltion-page.jpg?raw=true)

<br>

* **Checkout page**
------------------------------

- The user provides his information for the shipment and adds his payment information.
- At the bottom of the form, he can create an account or log in so that his data can be saved on his profile for future visits to the website.
- Next to the form there is a summary of the items to be purchased.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-cancaltion-page.jpg?raw=true)

- The very bottom of the page contains 2 buttons. One is for completing the order, and the other is to adjust the shopping bag. The total amount to be charged is presented under the "Complete Order" button.
- Clicking the "Complete Order" button will initiate a link to Stripe for completing the order.
- Click the "Adjust Bag" button will send the user back the shopping bag for editing the order.


![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

* **Thank you page**
------------------------------

- The page contains the user order details. The form has the following:
 * Summary of products purchased.
 * Order number and date.
 * Users' personal information.
 * Grand total broken down to product price and shipping price.
- At the top of the form he will see a confirmation line saying:
" Your order information is below. A confirmation email will be sent to {user email}."
- At the bottom of the form there is a caa=ll-to-action button that offers the user to check out the latest deal called "NOW CHECK OUT THE LATEST DEALS". The button will send the user to a page with products selected by the admin from any category he would like.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)



* **Write a review**
----------------------

- The page contains products that were pre-approved by the admin to be eligible for getting a review.
- The page is accessed through the "REVIEW" tab from the main navigation bar.
- Every product in that section has an image, title, short description, and a button called "RATE NOW" that redirects to the review form.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

* **Review form**
----------------------

- The review form contains 3 parts:
 * Auther title\name.
 * The star rating 1-5.
 * A comment section.
- The only mandatory fields are the star rating and comment fields.
- The author part has a default title of "anonymous".
- Once the form is complete, the user submits the review using the "RATE NOW" button.
- After submitting the form, the user will be redirected to a thank you page that has a "BACK TO OUR HOME PAGE" button and a "Thank you. Your review will be checked by the website owner." massage.



![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

* **My Profile**
----------------------

- The page contains 2 sections:
    - Profile information: The information extracted at the checkout page if the user created an account or has an account is stored on the left side of the page.
    - Previous orders: The right side contains all the users' past orders. The visible information includes the order date, order products, and the order amount.
    The order number is clickable and will redirect to order complete information.


![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)


### Admin Features
------------------

* **In the App**
----------------
- The admin has 3 options that can only be shown to the admin.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

Under every product there are 3 links:
Edit:
This page can be reached also from the Admin profile using the "Product Management" option.
On this page, there is a form with all the product attributes. The admin can edit any of them including uploading a new image. The same option exists in the admin panel under the "Products" model.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)

Delete:
This option will delete the product from the website.
This option has no additional warning, so precaution is advised.

Enable\Disable reviews:
This option can easily assist the admin in enabling and disabling a review.
The link is conveniently changing colors according to the current review state.
Yellow- means that the review is enabled.
Green- means that the review is disabled.


![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)


* **Admin panel**
-----------------

The Admin panel includes the following sections:

- ACCOUNTS- the admin can view, add, remove and edit any user email in the section.

 - AUTHENTICATION AND AUTHORIZATION- the admin can view, add, remove and edit any user in the section.
 He can see what are the users' permissions on the website and can grant him different access levels.

 - CHECKOUT- the admin can view, add, remove and edit any order in the section.
 
 - PRODUCTS- this section has two models in use:
    - Categories: the admin can view, add, remove and edit any category in the section.
    - Products: the admin can view, add, remove and edit any product in the section.

- REVIEWS- this section has two models in use:
    - Products: the admin can view, add, remove and edit any product in the section.
    - Reviews: the admin can view, add, remove and edit any review in the section.
    - Reviews: 

![admin panel email addresses list](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/admin-email-addresses.jpg?raw=true)

<br>

## Technologies Used
---------------------

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JS](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries and Programs Used

* [Font Awesome](https://fontawesome.com/)
     - Font Awesome was used throughout all pages to add icons in order to create a better visual experience for UX purposes.

* [GitPod](https://gitpod.io/)
     - GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/)
     - GitHub was used to store the project after pushing.

* [Balsamiq](https://balsamiq.com/)
     - Balsamiq was used to create the wireframes during the design phase of the project.

* [Am I Responsive?](http://ami.responsivedesign.is/#)
    - Am I Responsive was used in order to see responsive design throughout the process and to generate mockup imagery to be used.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    - W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - W3C CSS Validator was used to validate the CSS code.

* [PEP8](https://jigsaw.w3.org/css-validator/)
    - PEP8 was used to validate the python code.

* [STRIPE](https://stripe.com/)
    - STRIPE was used to process payments.

* [AWS](https://aws.amazon.com/)
    - AWS was used to store the databases in production and to create the user policy.

* [HEROKU](https://heroku.com/)
    - HEROKU was used to build the App for production.

* [MAILCHIMP](https://mailchimp.com/)
    - MAILCHIMP was used to create newsletter registarion for the website.

* [FACEBOOK](https://mailchimp.com/)
    - FACEBOOK was used to create social media account for the brand.


## Data Model
--------------

I have used six apps for this project, each servse a difernt porpuse:
- The bag app:
   * The app doesn't use database models.
   * The app has 4 views:
    - view_bag: renders the bag content.
    - add_to_bag: Add a quantity of the specified product to the shopping bag.
    - adjust_bag: Adjust the quantity of the specified product to the specified amount.
    - remove_from_bag: Remove the item from the shopping bag.

All the apps' functunality is revolve around the shopping bag signals.

- BookingListView class is in charge of presenting lists per site roles and permisssions:
   * If the user is a staff member, the function will return a list of the hotel bookings.
   * If the user is a logged-in user (authenticated), the function will present a list of all his bookings.

- RoomDetailView class is in charge of the following:
   * The class will create a booking form that contains check-in, check-out and a booking button.
   * The function will check if the form is valid and, if the room is available on the selected dates:
      - If the room is free, it will transfer the user to the booking confirmation page.
      - If the room is not free, he will get a message: "All of this category of rooms are booked! Try another one".
   * The function will check if the category exists. If it doesn't, the user will get the following massage:
   "Category does not exist, please go back and choose a valid category".

   - CancelBookingView class is in charge of:
      * Handling the room cancelation.
      * Returning the user to the booking_list_view.

     - UpdateBookingView class is in charge of:
      * Handling the room updates.
      * Returning the user to the booking_list_view.

   <br>

There are three database models:

   - Room_Categories:
      * This DB contains the room's name and description.
      * Its job is to create categories and to supply the initial descriptions of them.

   - Room:
      * This DB contains the actual room information within the category and contains the room number, what category it belongs to, how many beds it has and how many guests can sleep in it.
      * Its job is to supply information across the app.

   - Booking:
      * This DB contains the relationship between the user, the room, and the dates.
      * Its job is to supply the information for the booking form.

   <br>