import wx
from PIL import Image

THUMBNAIL_SIZE = (80, 80)


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window, on_drop_callback):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.on_drop_callback = on_drop_callback

    def OnDropFiles(self, x, y, filenames):
        for filename in filenames:
            self.on_drop_callback(filename)
        return True


class DragDropFrame(wx.Frame):
    def __init__(self, parent, title):
        super(DragDropFrame, self).__init__(
            parent, title=title, size=(600, 300))

        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        # Main panel for the application
        self.panel = wx.ScrolledWindow(self)
        # arbitrary large height to ensure scrolling
        self.panel.SetScrollbars(1, 1, 600, 2000)

        # Set the drop target to accept image files
        self.panel.SetDropTarget(MyFileDropTarget(self.panel, self.add_image))

        # Store the loaded images
        self.images = []

        # Vertical box sizer to organize widgets vertically
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Horizontal box sizer for thumbnails
        self.thumbnail_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Save button configuration
        save_button = wx.Button(self.panel, label="Save as PDF")
        save_button.Bind(wx.EVT_BUTTON, self.save_images_as_pdf)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(save_button)
        button_sizer.AddStretchSpacer()

        # Here, we first add the thumbnails sizer, then the button sizer, ensuring the button is at the bottom
        main_sizer.Add(self.thumbnail_sizer, 1,
                       flag=wx.EXPAND | wx.ALL, border=10)
        main_sizer.Add(button_sizer, 0, flag=wx.EXPAND | wx.BOTTOM, border=10)

        self.panel.SetSizer(main_sizer)

    def add_image(self, image_path):
        """Load and display a thumbnail of the dragged image."""
        img = Image.open(image_path)
        self.images.append(img)
        thumbnail = img.copy()
        thumbnail.thumbnail(THUMBNAIL_SIZE)

        wx_image = wx.Image(thumbnail.size[0], thumbnail.size[1])
        wx_image.SetData(thumbnail.tobytes())
        wx_image_thumbnail = wx.Bitmap(wx_image)

        bmp = wx.StaticBitmap(self.panel, -1, wx_image_thumbnail)
        self.thumbnail_sizer.Add(bmp, flag=wx.ALL, border=10)

        self.panel.Layout()

    def save_images_as_pdf(self, event):
        """Save all the dragged images into a single PDF."""
        if not self.images:
            wx.MessageBox("No images to save!", "Warning",
                          wx.OK | wx.ICON_WARNING)
            return

        save_path = wx.FileSelector("Save PDF As", wildcard="PDF files (*.pdf)|*.pdf",
                                    default_extension=".pdf", flags=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if save_path:
            self.images[0].save(save_path, save_all=True,
                                append_images=self.images[1:])
            wx.MessageBox("Images have been combined and saved as PDF!",
                          "Success", wx.OK | wx.ICON_INFORMATION)


app = wx.App(False)
frame = DragDropFrame(None, "Drag and Drop Images to Convert to PDF")
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
