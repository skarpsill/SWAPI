---
title: "Mate::GetMateEntities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetMateEntities.htm"
---

# Mate::GetMateEntities

This method is obsolete and has not been superseded.

Description

An assembly mate is always a relation between two entities. This method
returns those two mate entities. You can use these returned objects to
access the MateEntity interface, which provides methods for analyzing
the mate entity.

Syntax (OLE Automation)

retval = Mate.GetMateEntities ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing two Dispatch pointers to the MateEntity
objects |
| --- | --- | --- |

Syntax (COM)

status = Mate->IGetMateEntities
( &entity1, &entity2 )

(Table)=========================================================

| Output: | (LPMATEENTITY) entity1 | Pointer to the first MateEntity object |
| --- | --- | --- |
| Output: | (LPMATEENTITY) entity2 | Pointer to the second MateEntity object |
| Return: | (HRESULT)status | S_OK if successful |

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
<param name="Items" value="Mate_Object$$**$$Mate_Traversal$$**$$ZGetInfoMate$$**$$ZGetMateEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Mate\Mate__GetMateEntities.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
