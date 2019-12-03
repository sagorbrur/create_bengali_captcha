


from PIL import Image
import glob 





def generate_textfile(images_path):

	for img in images_path:
		img = Image.open(img)

		img_name = img.filename

		img_name_split = img_name.split('_')

		print(img_name_split)

		text_file = open(img_name_split[0]+'.txt', 'w')

		img_text = img_name_split[1][:-4]
		print(img_text)

		text_file.write(img_text)
		text_file.close()



if __name__=="__main__":
	images_path = glob.glob('data/train/*.png')
	generate_textfile(images_path)
