---
title: "MateEntity::GetEntityType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MateEntity/MateEntity__GetEntityType.htm"
---

# MateEntity::GetEntityType

This method is obsolete and has been superseded
by[MateEntity2::ReferenceType2](sldworksAPI.chm::/MateEntity2/MateEntity2__ReferenceType2.htm).

Description

This method returns the entity type for this mate entity.

Syntax (OLE Automation)

retval = MateEntity.GetEntityType ()

(Table)=========================================================

| Return: | (long) retval | Type of entity as defined in swMateEntityTypes_e |
| --- | --- | --- |

Syntax (COM)

status = MateEntity->GetEntityType
( &retval )

(Table)=========================================================

| Output: | (long) retval | Type of entity as defined in swMateEntityTypes_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Based on the entity type, you know what to expect in the Mate::GetMateParams
return value. To get to the MateEntity interface, use Mate::GetMateEntities.

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
<param name="Items" value="MateEntity$$**$$ZGetInfoMate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\MateEntity\MateEntity__GetEntityType.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
