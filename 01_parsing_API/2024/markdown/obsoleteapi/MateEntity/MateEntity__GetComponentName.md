---
title: "MateEntity::GetComponentName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MateEntity/MateEntity__GetComponentName.htm"
---

# MateEntity::GetComponentName

This method is obsolete and has been superseded
by[MateEntity2::ComponentName](sldworksAPI.chm::/MateEntity2/MateEntity2__ReferenceComponent.htm).

Description

This method gets the component name in the assembly associated with
this mate entity.

Syntax (OLE Automation)

retval = MateEntity.GetComponentName
()

(Table)=========================================================

| Return: | (BSTR) retval | Name of the component being
referenced by this MateEntity; the component name is in relation to the
assembly that owns this particular mate |
| --- | --- | --- |

Syntax (COM)

status = MateEntity->GetComponentName(
&retval )

(Table)=========================================================

| Output: | (BSTR) retval | Name of the component that is being referenced by this MateEntity; the
component name is in relation to the assembly that owns this particular
mate |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The component name returned is in relation to the assembly that owns
this mate entity.

For example, a typical assembly might be created with the following
components. The component names are as they might appear in the FeatureManager
design tree.

Assem1

|

--- Part1-1

|

--- Part1-2

|

--- Assem2-1

|

--- Part1-1

|

--- Part3-1

If there was a mate between Part1-1 and Part1-2 of Assem1, then the
component names returned for the MateEntity objects would be /Part1-1
and /Part1-2. If you also had a mate between Part1-1 of Assem1 and Part1-1
of Assem2-1, then the component names returned for the MateEntity objects
would be /Part1-1 and /Assem2-1/Part1-1. Each component name in any given
assembly is unique because it includes the relative path to any subassembly
components (for example, /Assem2-1/Part1-1).

When this particular mate is between a component and an assembly-level
feature, then MateEntity::GetComponentName returns a NULL string for the
component that contains the assembly-level feature. This only occurs when
the assembly-level feature is in the same assembly as the mate. If the
mate is between a component and an assembly-level feature in a subassembly,
then the subassembly component name is returned.

To get to the MateEntity interface used with this method, use Mate::GetMateEntities.

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
<param name="Items" value="MateEntity_Object$$**$$Mate_Traversal$$**$$ZGetInfoMate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\MateEntity\MateEntity__GetComponentName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
