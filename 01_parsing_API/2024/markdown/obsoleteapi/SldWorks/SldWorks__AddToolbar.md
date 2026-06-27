---
title: "SldWorks::AddToolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddToolbar.htm"
---

# SldWorks::AddToolbar

T his method is obsolete and has been superseded
by[SldWorks::AddToolbar2](SldWorks__AddToolbar2.htm).

Description

This method creates a Windows style, dockable toolbar, containing a
set of application defined buttons.

Syntax (OLE Automation)

retval = SldWorks.AddToolbar ( moduleName,
title, smallBitmapHandle, largeBitmapHandle )

(Table)=========================================================

| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (BSTR) title | Name of the toolbar |
| Input: | (long) smallBitmapHandle | Handle of the small bitmap image |
| Input: | (long) largeBitmapHandle | Handle of the large bitmap image |
| Return: | (long) retval | The toolbar ID for use with other methods or -1 if not created |

Syntax (COM)

status = SldWorks->AddToolbar (
moduleName, title, smallBitmapHandle, largeBitmapHandle, &retval )

(Table)=========================================================

| Input: | (BSTR)moduleName | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (BSTR) title | Name of the toolbar |
| Input: | (long)smallBitmapHandle | Handle of the small bitmap image |
| Input: | (long)largeBitmapHandle | Handle of the large bitmap image |
| Output: | (long)retval | The toolbar ID for use with other methods or -1 if not created |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method creates the ToolBar and passes the image for the buttons
to SolidWorks. To add functionality you must call SldWorks::AddToolbarCommand.

The bitmap images should contain the bitmaps for each of the buttons
(including separators) in the Toolbar as a single bitmap. For the small
bitmap the image for each button must be 16x15, for the large bitmap it
must be 22x22.

One way of creating the bitmaps is to add a Toolbar resource to your
Visual C++ project and then load the bitmap for that Toolbar into a Cbitmap
object, for example:

Example ToolBar resource in Visual C++

m_SmallToolbar.LoadMappedBitmap(IDR_TOOLBAR_SMALL);

HBITMAP hbmSmallImageWell = (HBITMAP)m_SmallToolbar.GetSafeHandle();

If you load your Toolbar image into a locally declared CBitmap object
in a function, then as the function returns and the local CBitmap is destroyed,
the handle passed to SolidWorks becomes invalid and, at best, the buttons
are blank.

NOTE:When your Add-In is unloaded, you
must call SldWorks::RemoveToolbar to remove this toolbar.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__AddToolbar.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Toolbar_Creation_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__AddToolbar.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
