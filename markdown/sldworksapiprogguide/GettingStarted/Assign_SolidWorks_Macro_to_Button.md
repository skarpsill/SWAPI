---
title: "Assign SOLIDWORKS Macro to Button"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Assign_SolidWorks_Macro_to_Button.htm"
---

# Assign SOLIDWORKS Macro to Button

When you create a SOLIDWORKS macro, you can assign a bitmap to a macro
button on a SOLIDWORKS toolbar. The SOLIDWORKS software includes sample
bitmaps, or you can create your own bitmap. If you create a bitmap for
a macro button, the bitmap must meet these requirements:

- Dimension = 16 x 16 pixels
- Color = 16 colors
- Background color = white

#### To assign a macro to a button:

1. With a document open, clickTools
  > Customize.
2. In the dialog box, on theCommandstab:
3. In theCustomizeMacroButtondialog box:

1. ClickChoose
  Image.
2. In theIcon
  pathdialog box, select a bitmap image (*.bmp),
  then clickOpen.NOTE:The SOLIDWORKS software provides bitmap images to use as custom
  buttons. These are located ininstall_dir/data/usermacro icons. SelectThumbnailto see the image in theIconpathdialog box.
3. Type aTooltipandPromptmessage, which should
  provide a brief description of the function of the tool on the status
  bar. Both the ToolTip and message are displayed when the pointer is on
  the bitmap.

1. SelectSW
  VBA Macros (*.swp)if adding a VBA macro (selected by default).

  - or -

  SelectSW VSTA Macros (*.dll)if
  adding a VB.NET or C# macro.

  **NOTE:**[SOLIDWORKS 2018 offers Visual Studio Tools for
  Applications (VSTA)](VSTA_2015.htm), impacting how you develop and run VB.NET and C#
  macros in SOLIDWORKS 2018 and later.
2. Select the macro.
3. ClickOpen.

1. ClickOKto close theCustomizedialog
  box.

#### To edit a macro button on a toolbar or CommandManager:

1. In an open SOLIDWORKS document, clickTools
  >Customize.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
2. If on a toolbar, right-click the macro button that you
  want to edit.
3. If in CommandManager, right-click the macro button that you want to edit.
  Select**Properties**.
4. In theCustomize
  Macro Buttondialog, edit the macro button and clickOK.
5. ClickOKto close theCustomizedialog.

#### To delete a macro button from a toolbar or CommandManager:

1. In an open SOLIDWORKS document, clickTools
  >Customize.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
2. If on a toolbar, drag and drop the macro button from
  the toolbar to the Recycle Bin.
3. If in CommandManager, right-click the macro button that you want to
  delete. Select**Delete**.
4. ClickOKto close theCustomizedialog.

For more information about assigning macros to toolbars, see SOLIDWORKS
Help.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic1" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="RecordSolidWorksMacro$$**$$EditSolidWorksMacro$$**$$RunSolidWorksMacro$$**$$AssignSolidWorksMacroShortcutKeyMenu$$**$$VBAMacroOverview$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\GettingStarted\Assign_SolidWorks_Macro_to_Button.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
