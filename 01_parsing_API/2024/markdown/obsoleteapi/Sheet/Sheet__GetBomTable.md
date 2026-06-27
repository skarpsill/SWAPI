---
title: "Sheet::GetBomTable"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__GetBomTable.htm"
---

# Sheet::GetBomTable

This
method is obsolete because BOM tables are now supported on a per view
basis. See[View::GetBomTable](sldworksAPI.chm::/View/View__GetBomTable.htm).

Description

This method returns the BOMTable object on the drawing sheet.

Syntax (OLE Automation)

retval = Sheet.GetBomTable ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the BomTable object |
| --- | --- | --- |

Syntax (COM)

status = Sheet->IGetBomTable ( &retval
)

(Table)=========================================================

| Output: | (LPBOMTABLE) retval | Pointer to the BomTable object |
| --- | --- | --- |
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
<param name="Items" value="Sheet_Object$$**$$ZGetBomTable$$**$$ZGetInfoBomTable$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Sheet\Sheet__GetBomTable.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
