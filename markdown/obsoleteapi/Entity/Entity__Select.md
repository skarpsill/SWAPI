---
title: "Entity::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Entity/Entity__Select.htm"
---

# Entity::Select

This
method is obsolete and has been superseded by[Entity::Select2](Entity__Select2.htm).

Description

This
method selects the entity and either appends it to the selection list
or replaces the entire selection list.

Syntax (OLE Automation)

retval
= Entity.Select ( appendFlag )

(Table)=========================================================

| Input: | (BOOL)
appendFlag | TRUE
if the entity is to be appended to the selection list, FALSE if the entity
replaces the selection list |
| --- | --- | --- |
| Return: | (BOOL)
retval | TRUE
if the entity was selected, FALSE if not |

Syntax (COM)

status
= Entity->Select ( appendFlag, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL)
appendFlag | TRUE
if the entity is to be appended to the selection list, FALSE if the entity
replaces the selection list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL)
retval | TRUE
if the entity was selected, FALSE if not |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

You can use this method to select features. In VC++, you must first
get the entity interface from the Feature object. To select features,
you can also use ModelDoc2::SelectByID with the feature name, feature
type and 0,0,0 coordinates.

You can use this method only with Entity objects that you get from the
active document. For example, if Assembly1 is the active document when
you call Entity::Select, then you must get the entity directly from the
Assembly1 document. You can do this using items in the selection list
(for example, SelectionMgr::GetSelectedObject3) or you can traverse the
body of an assembly component (for example, Component2::GetBody and Body2::GetFirstFace).
You cannot obtain the entity from the underlying part document (for example,
Component2::GetModelDoc,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PartDoc::Body,
and Body2::GetFirstFace).

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
<param name="Items" value="Entity_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Entity\Entity__Select.htm" >
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
<param name="Items" value="Entity_Select_Example$$**$$Get_Component_Face_By_Name_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Entity\Entity__Select.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
