# Step 1-1: Import the Pygame library
import pygame

# Step 4-1: Import random library
import random

# Step 6-1: Import time library
import time

# Step 1-2: setup the game window dimension
global width, height
width = 300
height = 300

# Step 1-3: Set the background color (RGB: 0, 0, 255): Blue
Background = (0, 0, 255)

# Step 1-4: Create the game window with the specified dimensions
screen = pygame.display.set_mode((width, height))

# Step 2-1: Defining the Player
play_colour = (0, 255, 0) #RGB color for player
play_width = 30 # size of the player square
play_height = 30 # size of the player square
global x, y # Global variables to store the player's position
x = width / 2 # Starting position at the center horizontally
y = height - 2 * play_height # Starting position near the bottom of the screen
play_speed = 15

# Step 2-2: Define a function called 'drawplayer()' to draw the player
def drawplayer():
    global player, x, y, play_speed
    
    # Create a Rectangle representating the player character using  the 'pygame.Rect()' function
    # The rectange is positioned at coordinates (x, y) with a width and height of 'play_size'
    player = pygame.Rect(x, y, play_width, play_height)
    
    # Step 3-1: Handle Keyboard Input for player Movement
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= play_speed # Move the player 5 pixel to the left
            elif event.key == pygame.K_RIGHT:
                x += play_speed # Move the player 5 pixel to the right
                
    # Step 3-2 Limit Player Movement within the screen boundaries
    # Ensure the player does not go outside the left edge of the screen
    if x < 0:
        x = 0
    # Ensure the player does not go outside the right edge of the screen
    if x > width - play_width:
        x = width - play_width
        
    # Draw the player rectangle on the 'screen' using the 'pygame.draw.rect()' function
    # The player character will be colored with the 'play_colour'.
    pygame.draw.rect(screen, play_colour, player)


# Step 4-2: Define the Enemy
# Define the color 'Red" using RGB values (255, 0, 0).
enemy_color = (255, 0, 0)

# Declare the global variables for enemy position and size
global x_e, y_e, enemy_width, enemy_height

# Set the initial size of the enemy to 20 pixels
enemy_width = 20
enemy_height = 20

# Set the initial x-coordinate of the enemy to a random value
x_e = random.randint(0, width - enemy_width)
# x_e = 0

# Set the initial y-coordinate of the enemy to 0 (at the top of the screen).
y_e = 0
# y_e = random.randint(0, width - enemy_width)

# Step 4-3: Define a function called 'drawenemy()' to draw the enemy on the screen
def drawenemy():
    global x_e, y_e, enemy_width, enemy_height, width, height, enemy
    
    # Create a rectangle representing the enemy using 'pygame.Rect()'.
    enemy = pygame.Rect(x_e, y_e, enemy_width, enemy_height)
    
    # Animate the Enemy Movement
    # Check if the enemy's y-coordinate is widthin the screen height.
    if y_e >= 0 and y_e < height:
       y_e += 5 # Move the enemy 5 pixels down
    # if x_e >= 0 and x_e < width:
    #     x_e += 5
        
    else:
        # Reset the Enemy Position
        y_e = 0 # Reset the y-coordinate to the top of the screen
        x_e = random.randint(0, width - enemy_width) # Appear at random x-coordinate
        # y_e = random.randint(0, height - enemy_height) # Appear at random x-coordinate
        # x_e = 0
        
    # Draw the enemy rectangle on the 'screen' using 'pygame.draw.rect()'.
    # The enemy will be colored with the 'Red' color.
    pygame.draw.rect(screen, enemy_color, enemy)
    # pygame.draw.ellipse(screen, enemy_color, enemy)

# Step 5-1: Initialize Pygame
pygame.init()

# Step 5-2: Initialize the score
global score # Declare a global variable to store the score
score = 0
collision_has_occured = False

def collision():
    global player, enemy, score, collision_has_occured # Declare variables as global for accessibility.
    
    # Step 5-4: Check for Collision
    # Check if the player's rectangle collides with the enemy's rectangle.
    if player.colliderect(enemy) and not collision_has_occured:
        score += 1 # Increase the score by 1 when a collision occurs.
        collision_has_occured = True
        
    if not player.colliderect(enemy):
        collision_has_occured = False
        
    # Step 5-5: Display the Score
    # Create a text label to display the current score.
    Text = 'Score: ' + str(score)
    
    # Define the font color using RGB values (255, 255, 0).
    font_color = (255, 255, 0)
    
    # Choose a font and size for the score label.
    myFont = pygame.font.SysFont("monospace", 25)
    
    # Create a rendered text label for the score using the chosen font and color.
    score_label = myFont.render(Text, 1, font_color)
    
    # Display the score label on the screen at coordinates (0, 0).
    screen.blit(score_label, (0, 0))

# Step 6-2: Initialize Game Variables
start_time = time.time() # Get the current time as the starting point
game_over = False # Initialize the game state as not over

# Step 6-3: Declare timer function
def timer():
    global start_time, game_over # Declare variables as global for accessibility
    
    # Calculate the total time elapsed since the game started
    total_time = time.time() - start_time
    
    # Step 6-4: Display Time on the Screen
    # Create a text label showing the elapsed time
    text = "Time: " + str(60 - int(total_time))
    
    # Choose a font and size for the time label
    myFont = pygame.font.SysFont("monospace", 25)
    
    # Render the time label using the chosen font and color (Black)
    time_label = myFont.render(text, 1, (255, 255, 0))
    
    # Display the time label on the screen, centered at the top
    global width
    screen.blit(time_label, (width / 2, 0))
    
    # Step 6-5: Check for Game Over Condition
    if total_time > 60:
        return True # If more than 30 seconds have passed, return True (game over)
    else:
        return False # If less than or equal to 30
    
# Step 8-1: Initialize Speed Power Up
spd_last_reset_time = time.time() - 4
spd_is_reset = True
spd_is_picked_up = False
spd_width = 30
spd_height = 30
spd_color = (255, 0, 255)
y_spd = 0
x_spd = random.randint(0, width - spd_width)

def update_speed_powerup():
    global speed_power_up, x_spd, y_spd, spd_width, spd_height, spd_is_reset, spd_last_reset_time, spd_is_picked_up, play_speed
    
    speed_power_up = pygame.Rect(x_spd, y_spd, spd_width, spd_height)
    
    if not spd_is_reset: # if speed power up is NOT reset
        if y_spd > height: # if power up y position is more than screen height
            spd_is_reset = True # set TRUE to speed power up is reset
            spd_last_reset_time = time.time() # set last time speed power up reset to Now
        else: # else move the power up downwards and draw the power up
            y_spd += 5  
            pygame.draw.ellipse(screen, spd_color, speed_power_up)
    
    if player.colliderect(speed_power_up) and not spd_is_reset: # if speed power up is NOT reset and player picked up speed power up
        play_speed = 30 # set the player speed to 30 pixels
        spd_is_reset = True # set TRUE to speed power up is reset
        spd_last_reset_time = time.time() # set last time speed power up reset to Now
        spd_is_picked_up = True
        
    if time.time() > spd_last_reset_time + 10 and spd_is_reset: # if speed power up is reset and elapsed more than 10 seconds since last time reset power up
        spd_is_reset = False # set FALSE to speed power up is reset
        y_spd = 0 # Reset the y-coordinate to the top of the screen
        x_spd = random.randint(0, width - spd_width) # Appear at random x-coordinate
        
    if time.time() > spd_last_reset_time + 5 and spd_is_picked_up: # if speed power up is picked up and elapsed more than 5 seconds since last time reset power up
        spd_is_picked_up = False # set FALSE to speed power up is picked up
        play_speed = 15 # reset the player speed back to 15 pixels
        
# Step 8-3: Initialize Expand Power Up
exp_last_reset_time = time.time()
exp_is_reset = True
exp_is_picked_up = False
exp_width = 30
exp_height = 30
exp_color = (0, 255, 255)
y_exp = 0
x_exp = random.randint(0, width - exp_width)

def update_expand_powerup():
    global expand_power_up, x_exp, y_exp, exp_width, exp_height, exp_is_reset, exp_last_reset_time, exp_is_picked_up, play_width
    
    expand_power_up = pygame.Rect(x_exp, y_exp, exp_width, exp_height)
    
    if not exp_is_reset: # if expand power up is NOT reset
        if y_exp > height: # if power up y position is more than screen height
            exp_is_reset = True # set TRUE to expand power up is reset
            exp_last_reset_time = time.time() # set expand power up last reset time  to Now
        else: # else move the power up downwards and draw the power up
            y_exp += 5
            pygame.draw.ellipse(screen, exp_color, expand_power_up)
    
    if player.colliderect(expand_power_up) and not exp_is_reset: # if expand power up is NOT reset and player picked up expand power up
        play_width = 60 # set the player width to 60 pixels
        exp_is_reset = True # set TRUE to expand power up is reset
        exp_last_reset_time = time.time() # set expand power up last reset time to Now
        exp_is_picked_up = True
        
    if time.time() > exp_last_reset_time + 10 and exp_is_reset: # if expand power up is reset and elapsed more than 10 seconds since power up last reset time 
        exp_is_reset = False # set FALSE to expand power up is reset
        y_exp = 0 # Reset the y-coordinate to the top of the screen
        x_exp = random.randint(0, width - exp_width) # Appear at random x-coordinate
    
    if time.time() > exp_last_reset_time + 5 and exp_is_picked_up: # if expand power up is picked up and elapsed more than 5 seconds since power up last reset time 
        exp_is_picked_up = False # set FALSE to expand power up is picked up
        play_width = 30 # reset the player width back to 30 pixels

# Step 1-5: Starting the game loop
# Step 6-6: Starting the game over loop
while not game_over:
    #Step 1-6: Fill the screen with the background color
    screen.fill(Background)
    
    #Step 2-3: Draw the player on the screen
    drawplayer()
    
    # Step 4-4: Call the enemy function
    drawenemy()
    
    # Step 5-6: Call the collision
    collision()
    
    # Step 6-7: Call the Time Function
    game_over = timer() # Call the 'timer()'
    
    # Step 8-2: Call the Update Extra Time Power Up Function
    update_speed_powerup()
    
    # Step 8-4: Call the Update Expand Power Up Function
    update_expand_powerup()
    
    pygame.time.delay(50) # Add a small delay to control the speed of the game.
    
    #Step 1-7: Update the display to show the changes made in this frame
    pygame.display.update()
    
# Step 7-1: Define Color Constants
Dark_blue = (0, 0, 255)
White = (255, 255, 255)

# Step 7-2: Fill the Screen with Dark Blue
screen.fill(Dark_blue) # Fill the entire screen with the Dark Blue color

# Step 7-3: Display "Game Over" Text
GO_text = 'Game Over' # Create a text string for the "Game Over" message

# Choose a font and size for the message
myFont = pygame.font.SysFont("monospace", 25)

# Render the "Game Over" message using the chosen font and color (White)
label = myFont.render(GO_text, 1, White)

# Display the message at coordinates (0, 0) on the screen
screen.blit(label, (88, 105))

# Step 7-4: Display Score Text
score_text = 'Score: ' + str(score) # Create a text string for the score display

# Choose a font and size for the score display
myFont = pygame.font.SysFont("monospace", 25)

# Render the score display using the chosen font and color (White)
label = myFont.render(score_text, 1, White)

# Display the score display at coordinates (0, 30) on the screen
screen.blit(label, (94, 135))

tryagain_text = 'Try Again!'

label = myFont.render(tryagain_text, 1, White)

screen.blit(label, (81, 165))

# Step 7-5: Update the Display
pygame.display.update() # Update the display to show the changes made


