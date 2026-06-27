---
title: "Sheet::GetOLEObjectData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__GetOLEObjectData.htm"
---

# Sheet::GetOLEObjectData

This method is obsolete and has been superseded
by[SwOLEObject](sldworksAPI.chm::/SwOLEObject/SwOLEObject.htm).

Description

This method gets data for an OLE object.

Syntax (OLE Automation)

void Sheet.GetOLEObjectData ( index, &buffer,
&retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (BYTE) buffer | Size of the byte array for the data object |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE otherwise |

Syntax (COM)

status = Sheet->IGetOLEObjectData ( index, &buffer,
&retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) index | Index of the OLE object |
| --- | --- | --- |
| Output: | (BYTE) buffer | Size of the byte array for the data object |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the buffer
data in the required format. These embedded objects are then saved with
the newly created drawing translation.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

This method only works with
an MFC DLL add-in because the buffer input parameter is assumed to point
to a Microsoft MFC object COleClientItem.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__GetOLEObjectData.htm" >
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
<param name="Items" value="Sheet Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Sheet\Sheet__GetOLEObjectData.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
