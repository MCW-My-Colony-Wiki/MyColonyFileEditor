from .exceptions import raise_TpE, raise_ISE, raise_ICE
from .tools.data import source_data, format_name

__all__ = [
	#Variants of built-in type
	'ListUnit',
	#Custom type
	'Source',
	'Category',
	'Unit',
	#Inherited from Unit
	'VideoTutorial',
	'Soundtrack',
	'Map',
	'Race',
	'Civilization',
	'Tile',
	'Resource',
	'Utility',
	'Occupation',
	'Terrain',
	'Technology',
	'Building',
	'Vehicle'
]

source_file_list = [
	'game',
	'strings'
]

#Pre-created source file data
source_file_data = {name: source_data(name) for name in source_file_list}

#Pre-filter out type(data) == list of dict
cat_to_unit_dict = {
	'videoTutorials': 'VideoTutorial',
	'soundtrack': 'Soundtrack',
	'mapTypes': 'Map',
	'races': 'Race',
	'civilizations': 'Civilization',
	'tiles': 'Tile',
	'resources': 'Resource',
	'utilities': 'Utility',
	'occupations': 'Occupation',
	'terrains': 'Terrain',
	'technology': 'Technology',
	'buildings': 'Building',
	'vehicles': 'Vehicle',
	'demands': None
}

#Variants of built-in type
class ListUnit:
	def __init__(self, category, data):
		#category check
		if type(category) is str:
			source = Source(source_file_list[0]) if category in source_file_data[source_file_list[0]].keys() else Source(source_file_list[1])
			category = Category(source, category)
			del source
		elif isinstance(category, Category):
			pass
		else:
			raise_TpE('category', Category)
		
		#data check
		if type(data) is list:
			#get unit(class)
			try:
				unit_class = eval(cat_to_unit_dict[category.name])
			except KeyError:
				#list
				for item in data:
					if type(item) != dict:
						raise_TpE('item in data', dict)
				#list of dict that not add to cat_to_unit_dict
				raise Warning(f"""Category '{category.name}' is temporarily unavailable, please report this issue to the developer on github.
Report issue here: https://github.com/Euxcbsks/mcp/issues

If you are a developer, please check source/game.js changes""")
		else:
			raise_TpE('data', list)
		
		self.category = category
		self.rdata = data
		self.data = [unit_class(category, item) for item in data]
		self.units = [unit.name if hasattr(unit, 'name') else unit.title for unit in self.data]
	
	def __getitem__(self, num_of_unit):
		if num_of_unit < len(self.data):
			return self.data[num_of_unit]
		raise StopIteration
	
	def __contains__(self, unit):
		if isinstance(unit, Unit) or type(unit) is str:
			try:
				unit = unit.name
			except AttributeError:
				pass
			
			return format_name(unit) in self.units
		return False
	
	def __str__(self):
		return self.category.name
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.units)

#Custom type
class Source:
	"""Content all data in specified source file
	
	Usage
	-----------
	- Create instance ::
		
		source = Source(source_file_name)
	
	'source_file_name' must be 'game' or 'strings'
	
	- for loop
		.. code-block:: python3
			
			for cate in Source:
				print(cate.name)
	
	'cate' is a `Category`
	
	Attributes
	-----------
	- name: name of this source file
	- data: all data in this source file
	- categories: all category in this source file
	
	Method
	-----------
	
	"""
	def __init__(self, name):
		#name check
		if type(name) != str:
			raise_TpE('name', str)
		if name not in source_file_list:
			raise_ISE(name)
		
		self.name = name
		self.data = source_file_data[name]
		self.categories = list(self.data.keys())
	
	def __getitem__(self, num_of_cat):
		if num_of_cat < len(self.categories):
			cat_name = self.categories[num_of_cat]
			return Category(self, cat_name)
		raise StopIteration
	
	def __contains__(self, category):
		if isinstance(category, Category) or type(category) is str:
			try:
				category = category.name
			except AttributeError:
				pass
			
			return category in self.data
		return False
	
	def __str__(self):
		return str(self.categories)
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.categories)

class Category:
	'''
	'''
	def __init__(self, source, name):
		#source check
		if type(source) is str:
			#If source is invalid, Source will raise_ISE
			#Don't need raise it here
			self.source = Source(source)
		elif isinstance(source, Source):
			self.source = source
		else:
			raise_TpE('source', Source)
		
		#name check
		if name in source.categories:
			self.name = name
		else:
			raise_ICE(name)
		
		#type(data) may be list(may contain dict or str) or dict
		data = source.data[name]
		
		#list of dict or list of str
		if type(data) is list:
			#list of dict
			try:
				data = ListUnit(self, data)
				self.units = data.units
			#list of str
			except TypeError: #as e:
				#print(e)
				pass
		#dict
		else:
			self.keys = list(data.keys())
		
		self.data = data
	
	def __getitem__(self, num_of_item):
		if num_of_item < len(self.data):
			#list of str or list of unit
			try:
				return self.data[num_of_item]
			#dict
			except KeyError:
				return self.keys[num_of_item]
		else:
			raise StopIteration
	
	def __contains__(self, item):
		if isinstance(item, Unit) or type(item) is str:
			return item in self.data
		return False
	
	def __str__(self):
		if hasattr(self, 'units'):
			return str(self.units)
		if hasattr(self, 'keys'):
			return str(self.keys)
		return str(self.data)
	
	def __repr__(self):
		self.__str__()
	
	def __len__(self):
		return len(self.data)

class Unit:
	def __init__(self, category, data):
		if isinstance(category, Category):
			self.source = category.source
			self.category = category
		else:
			raise_TpE('category', Category)
		
		if type(data) is dict:
			self.data = data
		else:
			raise_TpE('data', dict)
	
	def __str__(self):
		if hasattr(self, 'name'):
			return self.name
		if hasattr(self, 'title'):
			return self.title
		return str(self.data)
	
	def __repr__(self):
		self.__str__()

#Inherited from Unit
class VideoTutorial(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rtitle = self.data['title']
		self.title = format_name(self.rtitle)
		self.rauthor = self.data['author']
		self.author = format_name(self.rauthor)
		self.url = self.data['url']

class Soundtrack(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.title = self.data['title']
		self.file_format = self.data['format']
		self.seconds = self.data['seconds']

class Map(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.icon = self.data['icon']
		self.desc = self.data['description']
		self.ground = self.data['groundTile']
		self.terrains = self.data['terrainFeatures']
		self.difficulty = self.data['difficulty']
		self.techs = self.data['startingTechs']
		self.resources = self.data['startingResourceModifiers']
		self.buildings = self.data['startingBuildings']
		self.welcome = self.data['welcomeOverride']
		self.weather = self.data['weatherEffect']
		self.color = self.data['colorEffect']
		self.color_strength = self.data['colorStrength']
		self.river = self.data['riverTile']
		self.disasters = self.data['explosionDisasters']
		self.river_position = self.data['riverPosition']
		self.ocean = self.data['oceanTile']
		self.region = self.data['regionGroundTile']
		self.mapach = self.data['tenthousandColonistsMapAch']
		self.shores = self.data['groundShoreSheet']
		self.shore_connectors = self.data['groundShoreConnectors']
		self.river_color = self.data['mapRiverColor']

class Race(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.name = self.data['name']
		self.default = self.data['defaultSprites']
		self.tourist = self.data['touristSprites']
		self.student = self.data['studentSprites']
		self.retired = self.data['retiredSprites']
		self.techs = self.data['startingTechs']
		self.desc = self.data['description']
		self.narcotics = self.data['narcotics']
		self.color = self.data['raceColor']

class Civilization(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.desc = self.data['description']
		self.race = self.data['race']
		self.icon = self.data['icon']
		self.colonists = self.data['startingColonists']
		self.building = self.data['startingBuilding']
		self.vehicles = self.data['startingVehicles']
		self.techs = self.data['startingTechs']
		self.welcome = self.data['welcomeMessage']
		self.maps = self.data['availableMaps']
		self.server = self.data['serverHomeworld']
		self.resources = self.data['startingResourceModifiers']
		self.backstory = self.data['backstory']

class Tile(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.name = self.data['name']
		self.image = self.data['image']
		self.width = self.data['tileWidth']
		self.flip = self.data['canFlip']

class Resource(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.color = self.data['color']
		self.max = self.data['max']
		self.indicator = self.data['indicator']
		self.starting = self.data['starting']
		self.icon = self.data['icon']
		self.price = self.data['basePrice']
		self.essential = self.data['isEssential']
		self.amount = self.data['catchupAmount']
		self.toxic = self.data['toxicRate'] if 'toxicRate' in self.data else None
		self.gift = self.data['canGift']

class Utility(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.name = self.data['name']
		self.color = self.data['color']
		self.indicator = self.data['indicator']
		self.icon = self.data['icon']
		self.essential = self.data['isEssential']

class Occupation(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.tiles = self.data['tiles']
		self.salary = self.data['salary']
		self.indicator = self.data['indicator']

class Terrain(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.tile = self.data['tile']
		self.provides = self.data['provides']
		self.width = self.data['tileWidth']
		self.height = self.data['tileHeight']
		self.capacity = self.data['capacity']
		self.generates = self.data['generates']
		self.generate_time = self.data['generateTime']
		self.generate_amount = self.data['generateAmount']
		self.icon = self.data['icon']
		self.spread_rate = self.data['spreadRate']
		self.destruction_collect = self.data['collectOnDestruction']
		self.decay_rate = self.data['decayRate']
		self.light_effects = self.data['lightEffects']
		self.shore = self.data['shoreSheet']
		self.passable = self.data['passableConnectors']
		self.indestructable = self.data['indestructable']
		self.raid_items = self.data['raidItems']
		self.decays_to = self.data['decaysTo']
		self.spread_resource = self.data['spreadResource']
		self.additional_connectors = self.data['additionalConnectors']

class Technology(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.desc = self.data['description']
		self.icon = self.data['icon']
		self.cost = self.data['cost']
		self.techs = self.data['requiresTech']
		self.stage = self.data['requiresStage']
		self.independence = self.data['reqIndependence']
		self.premium = self.data['requiPremium']

class Building(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.tile = self.data['tile']
		self.cost = self.data['cost']
		self.desc = self.data['description']
		self.produces = self.data['produces']
		self.generates = self.data['generates']
		self.generate_time = self.data['generateTime']
		self.generate_amount = self.data['generateAmount']
		self.width = self.data['tileWidth']
		self.height = self.data['tileHeight']
		self.passable = self.data['passable']
		self.speed = self.data['driveSpeedMod']
		self.stores = self.data['stores']
		self.sell = self.data['sellValue']
		self.sell_warning = self.data['sellWarning']
		self.refines = self.data['refines']
		self.becomes_terrain = self.data['becomesTerrain']
		self.provides_utility = self.data['providesUtility']
		self.requires_utility = self.data['requiresUtility']
		self.col_gen_rate = self.data['colGenRate']
		self.shelter = self.data['providesShelter']
		self.chain = self.data['canChain']
		self.workers = self.data['acceptsWorkers']
		self.requires_workers = self.data['requiresWorkers']
		self.smelts = self.data['smelts']
		self.first_build_mes = self.data['firstBuildMessage']
		self.chop_shop = self.data['isChopShop']
		self.tax = self.data['earthTaxValue']
		self.tech = self.data['requiresTech']
		self.render_static = self.data['canRenderStatic']
		self.entertains = self.data['entertains']
		self.can_import = self.data['canImport']
		self.can_export = self.data['canExport']
		self.stage = self.data['requiresStage']
		self.occupation = self.data['occupation']
		self.indicator = self.data['indicator']
		self.upgrade = self.data['canUpgradeTo']
		self.transModeColor = self.data['transModeColor']
		self.fuel = self.data['requiresFuel']
		self.heals = self.data['heals']
		self.comms_hub_bldg = self.data['isCommsHubBldg']
		self.categories = self.data['buildCategories']
		self.independence = self.data['reqIndependence']
		self.online_trade_depot = self.data['onlineTradeDepot']
		self.sound = self.data['selectionSound']
		self.consulate = self.data['isConsulate']
		self.embassy = self.data['isEmbassy']
		self.limit = self.data['buildLimit']
		self.capitol = self.data['isCapitol']
		self.entertainmentCost = self.data['entertainmentCost']
		self.premium = self.data['requiPremium']
		self.embargo_immune = self.data['embargoImmune']
		self.tourists = self.data['takesTourists']
		self.tourist_doorway = self.data['touristDoorway']
		self.trade_capacity = self.data['tradeCapacity']
		self.upkeep_cost = self.data['upkeepCost']
		self.gift_capacity = self.data['giftCapacity']
		self.flip = self.data['canFlip']
		self.sign = self.data['isSign']
		self.unlocks_gov = self.data['unlocksGovLvl']
		self.default_house_cost = self.data['defaultHouseCost']
		self.requiresIQ = self.data['requiresIQ']
		self.educates = self.data['educates']
		self.providesIQ = self.data['providesIQ']
		self.stargate = self.data['isStargate']
		self.light_effects = self.data['lightEffects']
		self.packs_to = self.data['packsTo']
		self.can_build_over = self.data['canBuildOver']
		self.unlocks_achievement = self.data['unlocksAchievement'] if 'unlocksAchievement' in self.data else None
		self.jail_capacity = self.data['jailCapacity']
		self.transit_capacity = self.data['transitCapacity']
		self.subterranean_tile = self.data['subterraneanTile']
		self.transit_path = self.data['isTransitPath']
		self.connects_to = self.data['connectsTo']
		self.transit_unit = self.data['transitUnit']
		self.regional_port = self.data['isRegionalPort']
		self.creates_dec_units = self.data['createsDecUnits']

class Vehicle(Unit):
	def __init__(self, category, data):
		super().__init__(category, data)
		
		self.rname = self.data['name']
		self.name = format_name(self.rname)
		self.cost = self.data['cost']
		self.tile = self.data['tile']
		self.desc = self.data['description']
		self.produces = self.data['produces']
		self.sell = self.data['sellValue']
		self.sell_warning = self.data['sellWarning']
		self.harvests = self.data['harvests']
		self.capacity = self.data['capacity']
		self.tech = self.data['requiresTech']
		self.stage = self.data['requiresStage']
		self.indicator = self.data['indicator']
		self.build_categories = self.data['buildCategories']
		self.independence = self.data['reqIndependence']
		self.selection_sound = self.data['selectionSound']
		self.premium = self.data['requiPremium']
		self.first_build_mes = self.data['firstBuildMessage']
		self.speed = self.data['buildSpeed']
		self.deploys_to = self.data['deploysTo']
		self.fly = self.data['isFlying']
		self.vehicle_carry_capacity = self.data['vehicleCarryCapacity']
		self.colonist_carry_capacity = self.data['colonistCarryCapacity']
		self.canRaid = self.data['canRaid']
		self.move_confirm_sound = self.data['moveConfirmSound']
		self.harvest_confirm_sound = self.data['harvestConfirmSound']
		self.attack_confirm_sound = self.data['attackConfirmSound']
		self.deploy_confirm_sound = self.data['deployConfirmSound']
		self.build_confirm_sound = self.data['buildConfirmSound']
		self.creation_sound = self.data['creationSound']
