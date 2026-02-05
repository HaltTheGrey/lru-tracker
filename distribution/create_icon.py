"""
Icon Generator for LRU Tracker
Creates a custom .ico file with a warehouse/logistics theme
"""

from PIL import Image, ImageDraw
# Note: ImageFont and os imports removed as they're not currently used
# Can be added back if text rendering or file operations are needed

def create_lru_icon():
    """Create a custom icon for the LRU Tracker application"""
    
    # Create multiple sizes for the .ico file (Windows standard)
    sizes = [256, 128, 64, 48, 32, 16]
    images = []
    
    for size in sizes:
        # Create a new image with transparent background
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Define colors - FC/Warehouse theme
        bg_color = (41, 128, 185)      # Professional blue
        box_color = (236, 240, 241)     # Light gray for boxes
        text_color = (255, 255, 255)    # White
        border_color = (23, 32, 42)     # Dark border
        
        # Draw circular background
        margin = size // 10
        draw.ellipse([margin, margin, size-margin, size-margin], 
                     fill=bg_color, outline=border_color, width=max(1, size//32))
        
        # Draw a stack of boxes (representing LRU units)
        box_width = size // 3
        box_height = size // 6
        stack_x = (size - box_width) // 2
        
        # Draw 3 stacked boxes
        for i in range(3):
            y_offset = size // 3 + i * (box_height - 2)
            # Box shadow
            draw.rectangle([stack_x + 2, y_offset + 2, 
                          stack_x + box_width + 2, y_offset + box_height + 2],
                         fill=(0, 0, 0, 50))
            # Box
            draw.rectangle([stack_x, y_offset, 
                          stack_x + box_width, y_offset + box_height],
                         fill=box_color, outline=border_color, 
                         width=max(1, size//64))
        
        # Draw counter symbol badge
        check_x = size - size // 3
        check_y = size // 4
        
        # Draw a circular badge with number
        badge_radius = size // 6
        draw.ellipse([check_x - badge_radius, check_y - badge_radius,
                     check_x + badge_radius, check_y + badge_radius],
                    fill=(46, 204, 113), outline=border_color, 
                    width=max(1, size//64))
        
        # Draw count symbol (hash/number sign)
        if size >= 32:
            symbol_size = badge_radius // 2
            draw.line([check_x - symbol_size, check_y - symbol_size//2,
                      check_x + symbol_size, check_y - symbol_size//2],
                     fill=text_color, width=max(1, size//64))
            draw.line([check_x - symbol_size, check_y + symbol_size//2,
                      check_x + symbol_size, check_y + symbol_size//2],
                     fill=text_color, width=max(1, size//64))
            draw.line([check_x - symbol_size//2, check_y - symbol_size,
                      check_x - symbol_size//2, check_y + symbol_size],
                     fill=text_color, width=max(1, size//64))
            draw.line([check_x + symbol_size//2, check_y - symbol_size,
                      check_x + symbol_size//2, check_y + symbol_size],
                     fill=text_color, width=max(1, size//64))
        
        images.append(img)
    
    # Save as .ico file (in current directory)
    output_path = 'lru_icon.ico'
    images[0].save(output_path, format='ICO', sizes=[(s, s) for s in sizes])
    print(f"✓ Icon created: {output_path}")
    
    # Also save a PNG version for preview
    images[0].save('lru_icon.png', format='PNG')
    print(f"✓ Preview created: lru_icon.png")

if __name__ == "__main__":
    print("Creating LRU Tracker icon...")
    try:
        create_lru_icon()
        print("\n✓ Icon generation complete!")
        print("\nThe icon features:")
        print("  • Professional blue circular background")
        print("  • Stack of boxes (representing LRU units)")
        print("  • Green counter badge (representing tracking)")
        print("  • Multiple sizes for Windows compatibility")
    except ImportError:
        print("\n⚠ Pillow library not found!")
        print("\nInstalling Pillow...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'Pillow'])
        print("\nRetrying icon creation...")
        create_lru_icon()
        print("\n✓ Icon generation complete!")
