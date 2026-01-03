#!/usr/bin/env python3
"""
QR Code Generator - Fixed Version
This version includes error handling and installation guidance for missing dependencies.
"""

def install_qrcode_library():
    """Attempt to install qrcode library programmatically."""
    try:
        import subprocess
        import sys
        
        print("Attempting to install qrcode library...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "qrcode[pil]"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ qrcode library installed successfully!")
            return True
        else:
            print(f"✗ Installation failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Installation attempt failed: {e}")
        return False

def main():
    """Main QR code generation function."""
    try:
        # Try to import qrcode
        import qrcode
        print("✓ qrcode library is available!")
        
        # Get user input
        data = input('Enter the text or URL: ').strip()
        filename = input('Enter the filename (e.g., qrcode.png): ').strip()
        
        if not data:
            print("Error: Please enter some text or URL to encode.")
            return
        
        if not filename:
            filename = "qrcode.png"
        
        # Create QR code
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create image
        image = qr.make_image(fill_color='black', back_color='white')
        image.save(filename)
        
        print(f'✓ QR code saved as {filename}')
        print(f'  Data encoded: {data[:50]}{"..." if len(data) > 50 else ""}')
        
    except ImportError:
        print("✗ qrcode library is not installed.")
        print("\nTo fix this issue, please run one of these commands:")
        print("1. pip install qrcode[pil]")
        print("2. pip install qrcode pillow")
        print("3. python -m pip install qrcode[pil]")
        print("\nIf you have multiple Python installations, try:")
        print("  py -m pip install qrcode[pil]")
        print("  python3 -m pip install qrcode[pil]")
        print("\nAlternative: Try running from VS Code terminal where Python is properly configured.")
        
        # Try automatic installation
        if install_qrcode_library():
            print("\nRetrying QR code generation...")
            main()  # Recursive call to retry
        else:
            print("\nPlease install the qrcode library manually and try again.")
            
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    print("=== QR Code Generator ===")
    print("This tool generates QR codes from text or URLs.")
    print("-" * 40)
    main()
