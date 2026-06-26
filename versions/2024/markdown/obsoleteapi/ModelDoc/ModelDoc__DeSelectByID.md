---
title: "ModelDoc::DeSelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeSelectByID.htm"
---

# ModelDoc::DeSelectByID

This
method is obsolete and has been superseded by[ModelDoc2::DeSelectByID](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeSelectByID.htm).

Description

This method removes an already selected object from the selection list.

Syntax (OLE Automation)

retval = ModelDoc.DeSelectByID ( selID,
selParams, x, y, z)

(Table)=========================================================

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->DeSelectByID
( selID, selParams, x, y, z, &retval )

(Table)=========================================================

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__DeSelectByID.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
