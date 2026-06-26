---
title: "BomTable::GetRowCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BOMTable/BomTable__GetRowCount.htm"
---

# BomTable::GetRowCount

This method is obsolete and has been superseded
byBomTable::GetTotalRowCount .

Description

This method gets the number of rows in the BOM table.

Syntax (OLE Automation)

retval = BomTable.GetRowCount ()

(Table)=========================================================

| Return: | (long) retval | Number of rows in the BOM table |
| --- | --- | --- |

Syntax
(COM)

status = BomTable->GetRowCount (
&retval )

(Table)=========================================================

| Output: | (long) retval | Number of rows in the BOM table |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method only returns the visible rows in the BOM table.

Before you use any of the BomTable methods, activate the BOM Table using[BomTable::Attach](BomTable__Attach.htm). After you finish
getting BOM data, use BomTable::Detach to deactivate the table.

This method returns 0 if the BOM is obscured, which may occur when debugging
a macro. This is a quirk in Microsoft Excel, which is used by SolidWorks
for the BOM functionality.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="BomTable_Object$$**$$ZGetInfoBomTable$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\BOMTable\BomTable__GetRowCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
