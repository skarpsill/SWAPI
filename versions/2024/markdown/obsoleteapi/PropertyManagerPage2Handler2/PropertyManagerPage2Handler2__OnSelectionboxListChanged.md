---
title: "PropertyManagerPage2Handler2::OnSelectionboxListChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnSelectionboxListChanged.htm"
---

# PropertyManagerPage2Handler2::OnSelectionboxListChanged

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler3::OnSelectionboxListChanged](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnSelectionboxListChanged.htm).

Description

This method is called when the end-user changes
the selection list in a selection box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.OnSelectionboxListChanged
( Id, Count )

(Table)=========================================================

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection box |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnSelectionboxListChanged
( Id, Count )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection box |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is called when
your application uses a selection method, such as ModelDocExtension::SelectByID2,
just as if the selection was made interactively.

Regardless of how many items
the end-user selects, this method is called only once per interactive
box selection. In other words, if the end-user selects six faces using
a box selection, this method is called only once.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\PropertyManagerPage2Handler2\PropertyManagerPage2Handler2__OnSelectionboxListChanged.htm" >
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
<param name="Items" value="PropertyManagerPage2Handler2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\PropertyManagerPage2Handler2\PropertyManagerPage2Handler2__OnSelectionboxListChanged.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
