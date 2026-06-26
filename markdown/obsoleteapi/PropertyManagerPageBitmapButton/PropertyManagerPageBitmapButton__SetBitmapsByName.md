---
title: "PropertyManagerPageBitmapButton::SetBitmapsByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPageBitmapButton/PropertyManagerPageBitmapButton__SetBitmapsByName.htm"
---

# PropertyManagerPageBitmapButton::SetBitmapsByName

This method is obsolete and has been superseded
by[PropertyManagerPageBitmapButton::SetBitmapsByName2](sldworksAPI.chm::/PropertyManagerPageBitmapButton/PropertyManagerPageBitmapButton__SetBitmapsByName2.htm).

Description

This method sets the bitmaps
for this button.

Syntax (OLE Automation)

retval = PropertyManagerPageBitmapButton.SetBitmapsByName
( bitmapUp, bitmapDown, bitmapDisabled)

(Table)=========================================================

| Input: | (BSTR) bitmapUp | Path to the not pressed-in (up)
state bitmap image on disk |
| --- | --- | --- |
| Input: | (BSTR) bitmapDown | Path to the pressed-in (down)
state bitmap image on disk |
| Input: | (BSTR) bitmapDisabled | Path to the disabled state bitmap
image on disk |
| Output: | (VARIANT_BOOL*) retval | TRUE if the bitmap states are
set, FALSE if not |

Syntax (COM)

status = PropertyManagerPageBitmapButton->SetBitmapsByName
( bitmapUp, bitmapDown, bitmapDisabled, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) bitmapUp | Path to the not pressed-in (up) state bitmap
image on disk |
| --- | --- | --- |
| Input: | (BSTR) bitmapDown | Path to the pressed-in (down)
state bitmap image on disk |
| Input: | (BSTR) bitmapDisabled | Path to the disabled state bitmap
image on disk |
| Output: | (VARIANT_BOOL*) retval | TRUE if the bitmap
states are set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The bitmapUp, bitmapDown, and bitmapDisabled arguments
must be fully qualified paths to .bmp files on the disk. Relative paths
are not valid. The SolidWorks application loads the bitmaps from these
.bmp files and uses them on this bitmap button control.

You must call this method after calling either
of the following APIs to create the bitmap button control:

- PropertyManagerPage2::AddControl
- PropertyManagerPageGroup::AddControl

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\PropertyManagerPageBitmapButton\PropertyManagerPageBitmapButton__SetBitmapsByName.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PropertyManagerPageBitmapButton_Object$$**$$PropertyManagerPageBitmapButtonSet$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\PropertyManagerPageBitmapButton\PropertyManagerPageBitmapButton__SetBitmapsByName.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
