---
title: "eDConfiguration Class"
project: ""
interface: "eDConfiguration"
member: ""
kind: "class"
source: "emodeltoolkit/eDConfiguration/eDConfiguration_Class.htm"
---

# eDConfiguration Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Creates assembly, part, animation, set of exploded sets, name of a material,
mass properties, or hole properties.

#### Header file code

class eDConfiguration : public[eDObject](../eDObject/eDObject_Class.htm)

{

public:

eDOutcomebegin!kadov{{}}end!kadovCreatePart( constECHARbegin!kadov{{}}end!kadov*partname, const[eDAppearance](../eDAppearance/eDAppearance_Class.htm)&appearance,[eDPart](../eDPart/eDPart_Class.htm)*& part ); //Creates a
part

eDOutcomebegin!kadov{{}}end!kadovCreateAssembly( constECHARbegin!kadov{{}}end!kadov*assemblyname, const[eDAppearance](../eDAppearance/eDAppearance_Class.htm)&appearance,[eDAssembly](../eDAssembly/eDAssembly_Class.htm)*& assembly ); //Creates
an assembly

eDOutcomebegin!kadov{{}}end!kadovCreateAnimation( constECHARbegin!kadov{{}}end!kadov*animationname,[eDAnimation](../eDAnimation/eDAnimation_Class.htm)*&
animation ); //Creates an animation

eDOutcomebegin!kadov{{}}end!kadovCreateExplode( bool isplayed,[eDAnimation](../eDAnimation/eDAnimation_Class.htm)*& explode ); //Creates set of explode steps

eDOutcomebegin!kadov{{}}end!kadovSetMaterial( constECHARbegin!kadov{{}}end!kadov*material ); //Only sets the name; it is not associated with any material
data, like mass

eDOutcomebegin!kadov{{}}end!kadovSetMassProperties( const[eDMassProperties](../eDMassProperties/eDMassProperties_Class.htm)&massprops ); //Sets mass properties

eDOutcomebegin!kadov{{}}end!kadovAddHoleProperties( const[eDHoleProperties](../eDHoleProperties/eDHoleProperties_Class.htm)&holeprops ); //Adds hole properties

};

Metadata type="DesignerControl" startspan
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
<param name="Items" value="DocumentStructureClasses$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDConfiguration\eDConfiguration_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

kadov_tag{{<implicit_p>}}

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
<param name="Items" value="ZGeteDConfiguration$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDConfiguration\eDConfiguration_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
