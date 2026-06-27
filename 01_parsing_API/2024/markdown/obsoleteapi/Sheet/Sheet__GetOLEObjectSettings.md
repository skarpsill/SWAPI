---
title: "Sheet::GetOLEObjectSettings"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__GetOLEObjectSettings.htm"
---

# Sheet::GetOLEObjectSettings

This method is obsolete and has been superseded
by[SwOLEObject::Aspect](sldworksAPI.chm::/SwOLEObject/SwOLEObject__Aspect.htm),[SwOLEObject::Boundaries](sldworksAPI.chm::/SwOLEObject/SwOLEObject__Boundaries.htm),
and[SwOLEObject::Buffer](sldworksAPI.chm::/SwOLEObject/SwOLEObject__Buffer.htm).

Description

This method gets settings for an OLE object.

Syntax (OLE Automation)

retval = Sheet.GetOLEObjectSettings ( index, &byteCount,
&aspect )

(Table)=========================================================

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (long) byteCount | Size of the byte array for the data object |
| Output: | (long) aspect | Viewing aspect of the object ( uses DVASPECT
enumeration) |
| Return: | (VARIANT) retval | Box corner: top-left and bottom-right positions
in sheet coordinates |

Syntax (COM)

status = Sheet->IGetOLEObjectSettings ( index,
&byteCount, &aspect, &position, &retval )

(Table)=========================================================

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (long) byteCount | Size of the byte array for the data object |
| Output: | (long) aspect | Viewing aspect of the object ( uses DVASPECT
enumeration) |
| Output: | (double) position | Box corner: top-left and bottom-right positions
in sheet coordinates |
| Output: | (VARIANT_BOOL) retval | TRUE if the settings are successfully returned,
FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See the MSDN documentation
for details about the DVASPECT enumeration.

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
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__GetOLEObjectSettings.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Sheet_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__GetOLEObjectSettings.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXDeleteOLEObjectsDrawing$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__GetOLEObjectSettings.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
