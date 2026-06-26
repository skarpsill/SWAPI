---
title: "Mate::GetEntity"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetEntity.htm"
---

# Mate::GetEntity

This method is obsolete and has been superseded
by[Mate2::MateEntity](sldworksAPI.chm::/Mate2/Mate2__MateEntity.htm).

Description

This method gets an entity that is associated with an assembly mate.

Syntax (OLE Automation)

entity = Mate.GetEntity( whichOne )

(Table)=========================================================

| Input: | (int) whichOne | 0-based index of the entity associated with the mate |
| --- | --- | --- |
| Return: | (LPDISPATCH) entity | Dispatch pointer for the entity (face, edge and so on) or NULL if a
MateEntity is the origin of a component |

Syntax (COM)

status = Mate->IGetEntity ( whichOne,
&entity )

(Table)=========================================================

| Input: | (int) whichOne | 0-based index of the entity associated with the mate |
| --- | --- | --- |
| Output: | (LPENTITY) entity | Pointer to an Entity object (underlying face, edge and so on) or NULL
if a MateEntity is the origin of a component |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The Entity object returned is only valid in the
context of its owning mate. In other words, the Entity object returned
is only valid in the assembly that owns this mate. You cannot use this
Entity object at the PartDoc level.

Lightweight components are unable to return an
Entity object from this method. For more information, see Working With
Lightweight Components.

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
<param name="Items" value="Mate_Object$$**$$Mate_Traversal$$**$$ZGetInfoMate$$**$$ZGetMateEntity$$**$$Assembly_Analysis$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Mate\Mate__GetEntity.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
