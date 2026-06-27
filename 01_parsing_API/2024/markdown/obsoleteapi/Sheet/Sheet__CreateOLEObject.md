---
title: "Sheet::CreateOLEObject"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__CreateOLEObject.htm"
---

# Sheet::CreateOLEObject

This method is obsolete and has been superseded
by[ModelDocExtension::CreateOLEObject](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CreateOLEObject.htm).

Description

This method creates an OLE object from data.
This method is primarily intended to allow the translation of a drawing
that contains embedded objects.

Syntax (OLE Automation)

retval = Sheet.CreateOLEObject ( aspect, position,
buffer )

(Table)=========================================================

| Input: | (long) aspect | Viewing aspect of the object ( uses DVASPECT
enumeration) |
| --- | --- | --- |
| Input: | (VARIANT) position | Box corner top-left and bottom-right positions
in sheet coordinates |
| Input: | (VARIANT) buffer | Data for the OLE object |
| Return: | (BOOL) retval | TRUE if the object is successfully created, FALSE
if not |

Syntax (COM)

status = Sheet->CreateOLEObject ( aspect, &position,
byteCount, &buffer, &retval )

(Table)=========================================================

| Input: | (long) aspect | Viewing aspect of the object ( uses DVASPECT
enumeration) |
| --- | --- | --- |
| Input: | (double) position[6] | Box corner top-left and bottom-right positions
in sheet coordinates |
| Input: | (long) byteCount | Size of the byte array for the data object |
| Input: | (BYTE)* buffer | Data for the OLE object |
| Output: | (VARIANT_BOOL) retval | TRUE if the object is successfully created, FALSE
if not |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

See the MSDN documentation for details about the
DVASPECT enumeration.

The aspect argument uses the DVASPECT enumeration,
which has the following values:

- DVASPECT_CONTENT
  = 1
- DVASPECT_THUMBNAIL
  = 2
- DVASPECT_ICON
  = 4
- DVASPECT_DOCPRINT
  = 8

The buffer data is in the format obtained from
the Microsoft MFC object COleClientItem using the GetHGlobalFromILockBytes.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__CreateOLEObject.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Sheet_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__CreateOLEObject.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
